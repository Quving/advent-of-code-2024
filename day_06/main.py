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
        index = self.turn_order.index(self.current_direction)
        self.current_direction = self.turn_order[(index + 1) % 4]

    def move_forward(self):
        if self.current_direction == "N":
            self.y -= 1
        elif self.current_direction == "E":
            self.x += 1
        elif self.current_direction == "S":
            self.y += 1
        elif self.current_direction == "W":
            self.x -= 1

    def get_next_position(self):
        if self.current_direction == "N":
            return self.x, self.y - 1
        elif self.current_direction == "E":
            return self.x + 1, self.y
        elif self.current_direction == "S":
            return self.x, self.y + 1
        elif self.current_direction == "W":
            return self.x - 1, self.y


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
        for y in range(self.game_map.height):
            for x in range(self.game_map.width):
                if self.game_map.map[y][x] == '^':
                    print("Guard found at", x, y)
                    return x, y

    def is_valid_position(self, x, y):
        return 0 <= x < self.game_map.width and 0 <= y < self.game_map.height

    def get_marker(self, x, y):
        return self.game_map.map[y][x]

    def set_marker(self, marker, x, y):
        self.game_map.map[y][x] = marker

    def can_move_to(self, x, y):
        if not self.is_valid_position(x, y):
            return True
        return self.game_map.map[y][x] != '#'

    def start_walk(self):
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

            if self.can_move_to(*next_guard_pos):

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

    def print_map(self):
        for line in self.game_map.map:
            print(''.join(line))


def part_1(input_list):
    game = Game(game_map=GameMap(input_list), guard=Guard())
    walk_path = game.start_walk()

    distinct_positions = len(set([f"{x},{y}" for x, y, _ in [pos.split(',') for pos in walk_path]]))
    print("Distinct positions: ", distinct_positions)


def part_2(input_list):
    # From Part 1
    game = Game(game_map=GameMap(input_list), guard=Guard())
    walk_path = game.start_walk()

    # Mark visited positions
    marked_map = game.game_map.map
    visited_positions = []
    for i, line in enumerate(marked_map):
        for j, marker in enumerate(line):
            if marker in ['N', 'E', 'S', 'W']:
                visited_positions.append([i, j])
                marked_map[i][j] = '.'

    # Count infinite loops
    infinite_loops = 0
    for vp in visited_positions:
        marked_map_copy = [line.copy() for line in marked_map]

        # Replace the visited position with an obstacle
        marked_map_copy[vp[0]][vp[1]] = '#'

        game = Game(game_map=GameMap(marked_map_copy), guard=Guard(x=80, y=32, current_direction='N'))
        try:
            game.start_walk()
        except InfiniteLoopError:
            infinite_loops += 1

    print("Infinite loops: ", infinite_loops)


if __name__ == '__main__':
    input_list = read_input()

    # Convert input to a list of lists
    input_list = [list(line) for line in input_list]

    # Important: Copy the input_list for part_1 and part_2!
    part_1(input_list=[line.copy() for line in input_list])
    part_2(input_list=[line.copy() for line in input_list])
