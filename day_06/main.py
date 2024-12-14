#!/usr/bin/env python3
""" Day 06 - Advent of Code 2024 """


def read_input():
    with open("day_06/input.txt", "r") as file:
        return [line.strip() for line in file]


class InfiniteLoopError(Exception):
    pass


class Guard:
    def __init__(self, x=None, y=None, current_direction="N"):
        self.x = x
        self.y = y
        self.current_direction = "N"
        self.turn_order = ["N", "E", "S", "W"]

    def turn_right(self):
        """
        Change the direction of the guard to the right
        :return:
        """
        index = self.turn_order.index(self.current_direction)
        self.current_direction = self.turn_order[(index + 1) % 4]

    def move_forward(self):
        """
        Move the guard forward in the current direction 1 step
        :return:
        """
        if self.current_direction == "N":
            self.y -= 1
        elif self.current_direction == "E":
            self.x += 1
        elif self.current_direction == "S":
            self.y += 1
        elif self.current_direction == "W":
            self.x -= 1
        else:
            raise ValueError("Invalid direction")

    def get_next_position(self):
        """
        Get the next position of the guard depending on the current direction and current position
        :return:
        """
        if self.current_direction == "N":
            return self.x, self.y - 1
        elif self.current_direction == "E":
            return self.x + 1, self.y
        elif self.current_direction == "S":
            return self.x, self.y + 1
        elif self.current_direction == "W":
            return self.x - 1, self.y
        else:
            raise ValueError("Invalid direction")


class GameMap:
    def __init__(self, game_map: list[list[str]]):
        self.map = game_map
        self.width = len(game_map[0])
        self.height = len(game_map)


class Game:
    def __init__(self, game_map: GameMap, guard: Guard):
        self.game_map = game_map
        self.game_map_original = [line.copy() for line in game_map.map]
        self.guard = guard

        if self.guard.x is None and self.guard.y is None:
            self.guard.x, self.guard.y = self.find_guard_position()

    def find_guard_position(self):
        """
        Locate the guard position in the map and return the x, y coordinates or None
        :return:
        """
        for y in range(self.game_map.width):
            for x in range(self.game_map.height):
                if self.game_map.map[x][y] == '^':
                    print("Guard found at", x, y)
                    return x, y

    def is_valid_position(self, x, y):
        """
        Check if the position is within the map boundaries
        :param x:
        :param y:
        :return:
        """
        return 0 <= x < self.game_map.width and 0 <= y < self.game_map.height

    def get_marker(self, x, y):
        """
        Get the marker at the position x, y
        :param x:
        :param y:
        :return:
        """
        return self.game_map.map[x][y]

    def set_marker(self, marker, x, y):
        """
        Set a new marker at the position x, y
        :param marker:
        :param x:
        :param y:
        :return:
        """
        self.game_map.map[x][y] = marker

    def is_blocked_by_obstacle(self, x, y):
        """
        Return True if the position is blocked by an obstacle indicated by '#'
        :param x:
        :param y:
        :return:
        """
        if not self.is_valid_position(x, y):
            return True
        return self.game_map.map[x][y] != '#'

    def start_walk(self):
        """
        Start the walk and return the visited positions (can take a while)
        :return:
        """
        steps_count = 0
        visited_positions = set()

        while True:
            next_guard_pos = self.guard.get_next_position()
            curr_guard_pos = self.guard.x, self.guard.y

            # Check if guard has visited this position before
            bread_crumb = f"{self.guard.x},{self.guard.y},{self.guard.current_direction}"
            if bread_crumb in visited_positions:
                raise InfiniteLoopError("Infinite loop detected")

            # Update visited positions
            visited_positions.add(bread_crumb)

            if self.is_blocked_by_obstacle(*next_guard_pos):

                # Mark current position before moving (only once)
                if self.get_marker(*curr_guard_pos) in ['.', '^']:
                    self.set_marker(self.guard.current_direction, *curr_guard_pos)
                    steps_count += 1

                self.guard.move_forward()
            else:
                self.guard.turn_right()

            # Cancel if guard has left map
            if not self.is_valid_position(self.guard.x, self.guard.y):
                return visited_positions


def part_1(input_list):
    """
    Part 1
    :param input_list:
    :return:
    """
    game = Game(game_map=GameMap(input_list), guard=Guard())
    walk_path = game.start_walk()

    distinct_positions = len(set([(int(x), int(y)) for x, y, _ in [pos.split(',') for pos in walk_path]]))
    print("Distinct positions: ", distinct_positions)


def part_2(input_list):
    """
    Part 2
    :param input_list:
    :return:
    """
    # From Part 1
    game = Game(game_map=GameMap([line.copy() for line in input_list]), guard=Guard())
    path_walked = game.start_walk()

    distinct_positions_pos = set([(int(x), int(y)) for x, y, _ in [pos.split(',') for pos in path_walked]])

    # Count infinite loops
    infinite_loops = 0
    for vp in distinct_positions_pos:
        game_map_copy = [line.copy() for line in input_list]

        # Replace the visited position with an obstacle
        game_map_copy[vp[0]][vp[1]] = '#'

        # Run the game and count infinite loops
        game = Game(game_map=GameMap(game_map_copy), guard=Guard(x=80, y=32, current_direction='N'))
        try:
            game.start_walk()
        except InfiniteLoopError:
            infinite_loops += 1

    print("Infinite loops: ", infinite_loops)


if __name__ == '__main__':
    task_input = read_input()

    # Convert lines to columns and to a list of lists.
    task_input = [list(line) for line in task_input]
    task_input = list(map(list, zip(*task_input)))

    # Important: Copy the input_list for part_1 and part_2!
    part_1(input_list=[line.copy() for line in task_input])
    part_2(input_list=[line.copy() for line in task_input])
