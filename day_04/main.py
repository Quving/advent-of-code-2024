def read_input():
    with open("day_04/input.txt", "r") as file:
        return [line.strip() for line in file]


def slide_and_count_matches(line: str, word: str):
    matches = 0
    for i in range(len(line) - len(word) + 1):
        if line[i:i + len(word)] == word:
            matches += 1

    return matches


def part_1():
    match_words = ["XMAS", "SAMX"]

    input_list = read_input()
    # input_list = [list(line) for line in input_list]
    all_words = []

    width = len(input_list[0])
    height = len(input_list)

    # Collect horizontally
    for line in input_list:
        all_words.append(line)

    # Collect vertically
    for i in range(width):
        word = []
        for j in range(height):
            word.append(input_list[j][i])
        all_words.append(''.join(word))

    # Collect diagonally
    all_words += get_diagonals_from_2d_list(input_list)

    # Count matches in all sentences
    matches = 0
    for word in all_words:
        for match_word in match_words:
            matches += slide_and_count_matches(word, match_word)

    print(f"Matches: {matches}")


def get_diagonals_from_2d_list(matrix):
    diags = []
    width = len(matrix[0])
    height = len(matrix)

    for i in range(width):

        # Walk diagonally from top left to bottom right
        chars = ''
        i1, j1 = i, 0
        while i1 < width and j1 < height:
            chars += matrix[j1][i1]
            i1 += 1
            j1 += 1
        diags.append(chars)

        # Walk diagonally from top right to bottom left
        chars = ''
        i1, j1 = i, 0
        while i1 >= 0 and j1 < height:
            chars += matrix[j1][i1]
            i1 -= 1
            j1 += 1
        diags.append(chars)

    for j in range(1, height):
        # Walk diagonally from top left to bottom right
        chars = ''
        i1, j1 = 0, j
        while i1 < width and j1 < height:
            chars += matrix[j1][i1]
            i1 += 1
            j1 += 1
        diags.append(chars)

        # Walk diagonally from top right to bottom left
        chars = ''
        i1, j1 = width - 1, j
        while i1 >= 0 and j1 < height:
            chars += matrix[j1][i1]
            i1 -= 1
            j1 += 1
        diags.append(chars)

    return diags


def part_2():
    input_list = read_input()

    def get_diagonal_neighbors(x, y, matrix):
        diagonals = [
            (x - 1, y - 1),  # Top left
            (x + 1, y + 1),  # Bottom right
            (x - 1, y + 1),  # Bottom left
            (x + 1, y - 1),  # Top right
        ]

        # Remove invalid diagonals (out of bounds)
        return [d for d in diagonals if 0 <= d[0] < len(matrix) and 0 <= d[1] < len(matrix[0])]

    # Approach: Search an A. Each A must have 2 S's and 2 M's diagonally.
    matches = 0
    for i in range(1, len(input_list) - 1):
        for j in range(1, len(input_list[i]) - 1):
            if input_list[i][j] == 'A':
                neighbors_indices = get_diagonal_neighbors(i, j, input_list)
                neighbors = [input_list[n[0]][n[1]] for n in neighbors_indices]

                # Valid neighbors patterns
                valid_patterns = [
                    ['S', 'M', 'S', 'M'],
                    ['S', 'M', 'M', 'S'],
                    ['M', 'S', 'M', 'S'],
                    ['M', 'S', 'S', 'M'],
                ]

                if neighbors in valid_patterns:
                    matches += 1

    print(f"Matches: {matches}")


if __name__ == '__main__':
    list_simplified = [
        ["A", "M", "M"],
        ["A", "B", "X"],
        ["X", "M", "A"],
    ]
    diagonals_expected = [
        'ABA', 'A', 'MX', 'MA', 'M', 'MBX', 'AM', 'A', 'X', 'X'
    ]

    # print(get_diagonals_from_2d_list(list_simplified))

    part_1()
    part_2()
