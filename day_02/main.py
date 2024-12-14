#!/usr/bin/env python3
""" Day 02 - Advent of Code 2024 """


def read_input() -> list[list[int]]:
    x = []
    with open("day_02/input.txt") as f:
        for line in f:
            x.append(list(map(int, line.strip().split())))
    return x


def is_monotonic(row: list[int]) -> bool:
    increasing = []
    decreasing = []
    for i in range(1, len(row)):
        if row[i - 1] > row[i]:
            increasing.append(False)
            decreasing.append(True)
        elif row[i - 1] < row[i]:
            increasing.append(True)
            decreasing.append(False)
        else:
            increasing.append(False)
            decreasing.append(False)

    return all(increasing) or all(decreasing)


def is_steep_enough(row: list[int]) -> bool:
    all_steepness = []
    for i in range(1, len(row)):
        steepness = abs(row[i] - row[i - 1])
        all_steepness.append(1 <= steepness <= 3)

    return all(all_steepness)


def part_1(list_input: list[list[int]]):
    counter_safe_ways = 0

    for row in list_input:
        if is_monotonic(row) and is_steep_enough(row):
            counter_safe_ways += 1

    print("Total safe ways: ", counter_safe_ways)


def part_2(list_input: list[list[int]]):
    counter_safe_ways = 0

    for row in list_input:
        if is_monotonic(row) and is_steep_enough(row):
            counter_safe_ways += 1
        else:
            for i in range(0, len(row)):
                new_row = row[:i] + row[i + 1:]
                if is_monotonic(new_row) and is_steep_enough(new_row):
                    counter_safe_ways += 1
                    break  # We only need to find one in each row

    print("Total safe ways with removing 1 step: ", counter_safe_ways)


if __name__ == '__main__':
    input_list = read_input()
    part_1(input_list)
    part_2(input_list)
