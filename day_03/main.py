def read_input():
    with open("day_03/input.txt", "r") as file:
        return [line.strip() for line in file]


def part_1(task_input: list[str]):
    import re
    regex = r"mul\(\d+,\d+\)"

    sum_of_all_lines = 0
    for line in task_input:
        matches = re.findall(regex, line)

        for match in matches:
            a, b = [re.findall(r'\d+', m) for m in match.split(',')]

            sum_of_all_lines += int(a[0]) * int(b[0])

    print("Sum of all: ", sum_of_all_lines)


if __name__ == '__main__':
    input_list = read_input()
    part_1(input_list)
