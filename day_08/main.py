#!/usr/bin/env python3
""" Day 08 - Advent of Code 2024 """
import itertools


def read_input() -> list[list[str]]:
    with open("day_08/input.txt", "r", encoding='utf-8') as file:
        return [list(line.strip()) for line in file]


def part_1():
    """
    Part 1:
    Approach: For each frequency, calculate the antinodes and mark them with a '#'
    To do so: Collect each frequency's coordinates and calculate the antinodes by its path to each other.
    :return:
    """
    list_list = read_input()
    # Transpose list to columns to easy handle of x,y coordinates
    list_list = list(map(list, zip(*list_list)))

    # Store the coordinates of each frequency
    frequency_coordinates = {}
    for x, y in itertools.product(range(len(list_list[0])), range(len(list_list))):
        c = list_list[x][y]

        if c in ['.', '#']: continue  # Skip empty cells

        if c in frequency_coordinates:
            frequency_coordinates[c] += [(x, y)]
        else:
            frequency_coordinates[c] = [(x, y)]

    antinodes_coords = set()  # Use a set to ignore duplicates
    for f, coords in frequency_coordinates.items():
        tuples = list(itertools.product(coords, coords))

        # Eliminate duplicate tuples (a,a), (b,b), etc.
        tuples = [t for t in tuples if t[0] != t[1]]

        for a, b in tuples:
            x_diff = b[0] - a[0]
            y_diff = b[1] - a[1]

            # Compute the distance between the two frequencies and calculate the antinodes
            # before the first and behind the second frequency
            a_nodes = [
                (a[0] - x_diff, a[1] - y_diff),
                (b[0] + x_diff, b[1] + y_diff)
            ]

            for an in a_nodes:
                # Skip antinodes outside the grid
                if not (0 <= an[0] < len(list_list[0])) and (0 <= an[1] < len(list_list)):
                    continue

                antinodes_coords.add(an)  # Count it

                # Mark antinode with '#' on grid. Do not overwrite existing frequencies.
                marker_current = list_list[an[0]][an[1]]
                if marker_current not in frequency_coordinates.keys(): list_list[an[0]][an[1]] = "#"

    # Transpose list back to rows to print.
    list_list = list(map(list, zip(*list_list)))
    for line in list_list:
        print(''.join(line))

    print("Count: ", len(antinodes_coords))


if __name__ == '__main__':
    part_1()  # 369
