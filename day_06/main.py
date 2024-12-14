def read_input():
    with open("day_06/input.txt", "r") as file:
        return [line.strip() for line in file]


class Guard:
    def __init__(self):
        self.x = None
        self.y = None
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
        self.guard = guard

        self.guard.x, self.guard.y = self.find_guard_position()
        print("Guard position: ", self.guard.x, self.guard.y)

    def find_guard_position(self):
        for y in range(self.game_map.height):
            for x in range(self.game_map.width):
                if self.game_map.map[y][x] == '^':
                    return x, y

    def is_guard_on_map(self):
        return 0 <= self.guard.x < self.game_map.width and 0 <= self.guard.y < self.game_map.height

    def can_move_forward(self):
        x, y = self.guard.get_next_position()
        return self.game_map.map[y][x] != '#'

    def start_walk(self):
        steps = 0  # Current position counts as a step

        while True:
            if self.can_move_forward():
                # Mark current position before moving
                if self.game_map.map[self.guard.y][self.guard.x] != "X":
                    self.game_map.map[self.guard.y][self.guard.x] = 'X'
                    steps += 1

                self.guard.move_forward()
            else:
                self.guard.turn_right()

            # Cancel if guard has left map
            if not self.is_guard_on_map():
                print(f"Guard has left the map at {self.guard.x, self.guard.y}. Total steps: {steps}")
                break

    def print_map(self):
        for line in self.game_map.map:
            print(''.join(line))


if __name__ == '__main__':
    input_list = read_input()

    # Convert input to a list of lists
    input_list = [list(line) for line in input_list]

    game = Game(game_map=GameMap(input_list), guard=Guard())
    game.start_walk()
    # game.print_map()
