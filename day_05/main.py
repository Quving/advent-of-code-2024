#!/usr/bin/env python3
""" Day 05 - Advent of Code 2024 """
from functools import cmp_to_key


def read_input():
    with open("day_05/input.txt", "r", encoding='utf-8') as file:
        rules = []
        lines = []
        rules_end = False
        for line in file:
            if line == '\n':
                rules_end = True
                continue

            if not rules_end:
                rules.append([int(e.strip()) for e in line.split('|')])
            else:
                lines.append([int(e.strip()) for e in line.split(',')])

        return rules, lines


def is_line_correct(line, rules_dict) -> bool:
    for i in range(len(line) - 1):
        num_tail = rules_dict[line[i]]
        line_tail = line[i + 1:]

        for lt in line_tail:
            if lt not in num_tail:
                return False

    return True


def part_1(rules: dict, lines: list):
    """
    Approach:
    - Collect all rules in a dictionary. The key is the first number and the following number are put in a list.
    - For each line, check if the next number is in the list of the current number. If not, the line is incorrect.
    """

    # Check if the line is correct
    sum_of_correct_lines = 0
    for line in lines:
        if is_line_correct(line, rules):
            index_mid = len(line) // 2
            sum_of_correct_lines += line[index_mid]

    print("Part 1: Sum of all correct lines: ", sum_of_correct_lines)


def sort_line_correctly(line: list, rules: dict):
    def comp(a, b):
        if b in rules[a]:
            return -1
        return 1

    return sorted(line, key=cmp_to_key(comp))


def part_2(rules: dict, lines: list):
    # Check if the line is correct
    sum_of_incorrect_lines = 0
    for line in lines:
        if is_line_correct(line, rules):
            continue

        # Fix line by sorting the line correctly.
        line = sort_line_correctly(line, rules)

        # Check if the line is correct now
        if is_line_correct(line, rules):
            index_mid = len(line) // 2
            sum_of_incorrect_lines += line[index_mid]

    print("Part 2: Sum of all incorrect lines: ", sum_of_incorrect_lines)


if __name__ == '__main__':
    rules_list, lines_list = read_input()

    # Create a dictionary with the rules
    rules_dict = {}
    for rule in rules_list:
        if rule[0] in rules_dict:
            rules_dict[rule[0]].append(rule[1])
        else:
            rules_dict[rule[0]] = [rule[1]]

    part_1(rules_dict, lines_list)
    part_2(rules_dict, lines_list)
