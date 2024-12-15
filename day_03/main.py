#!/usr/bin/env python3
""" Day 03 - Advent of Code 2024 """

import re


def read_input():
    """
    Read input from file and return as a list of strings
    :return:
    """
    with open("day_03/input.txt", "r", encoding='utf-8') as file:
        return [line.strip() for line in file]


def compute_muls_in_string(string: str) -> int:
    """
    Given a string, compute the sum of all muls in the string and return it
    :param string:
    :return:
    """
    regex = r"mul\(\d+,\d+\)"

    sum_of_all_lines = 0
    matches = re.findall(regex, string)

    for match in matches:
        a, b = [re.findall(r'\d+', m) for m in match.split(',')]
        sum_of_all_lines += int(a[0]) * int(b[0])

    return sum_of_all_lines


def part_1(input_list: list[str]):
    """
    Part 1
    :param input_list:
    :return:
    """
    sum_of_all_lines = 0
    for line in input_list:
        sum_of_all_lines += compute_muls_in_string(line)

    print("Sum of all: ", sum_of_all_lines)


def part_2(line: str):
    """
    Part 2
    :param line:
    :return:
    """
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
    task_input = read_input()
    part_1(task_input)

    # Ignore newlines and append input_list to a single string
    task_input = ''.join(task_input)
    part_2(task_input)
