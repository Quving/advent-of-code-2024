#!/usr/bin/env python3
""" Day 03 - Advent of Code 2024 """


def read_input():
    with open("day_03/input.txt", "r") as file:
        return [line.strip() for line in file]


def compute_muls_in_string(string: str):
    import re
    regex = r"mul\(\d+,\d+\)"

    sum_of_all_lines = 0
    matches = re.findall(regex, string)

    for match in matches:
        a, b = [re.findall(r'\d+', m) for m in match.split(',')]
        sum_of_all_lines += int(a[0]) * int(b[0])

    return sum_of_all_lines


def part_1(task_input: list[str]):
    sum_of_all_lines = 0
    for line in task_input:
        sum_of_all_lines += compute_muls_in_string(line)

    print("Sum of all: ", sum_of_all_lines)


def part_2(line: str):
    import re
    matches = []

    regex_do_dont = r"do\(\).*?don't\(\)|^.*?don't\(\)"
    matches += re.findall(regex_do_dont, line)

    # Count muls in all matches
    matches = set(matches)
    sum_of_line = 0
    for match in matches:
        print(match)
        print()
        sum_of_line += compute_muls_in_string(match)

    print("Sum of all: ", sum_of_line)


if __name__ == '__main__':
    input_list = read_input()
    part_1(input_list)

    # Ignore newlines and append input_list to a single string
    input_list = ''.join(input_list)
    part_2(input_list)
