#!/usr/bin/env python3
""" Day 08 - Advent of Code 2024 """
import itertools


def read_input() -> list[list[str]]:
    with open("day_08/input.txt", "r", encoding='utf-8') as file:
        return [list(line.strip()) for line in file]


def part_1_and_2():
    """
    Part 1:
    Approach: For each frequency, calculate the antinodes and mark them with a '#'
    To do so: Collect each frequency's coordinates and calculate the antinodes by its path to each other.
    Part 2:
    Approach: The same procedure as part 1, but this time we put antinodes on the same path until the grid ends in
    each direction and count them including the frequencies themselves (+2) for each path.
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

    a_node_coords = set()  # Use a set to ignore duplicates
    for f, coords in frequency_coordinates.items():
        tuples = list(itertools.product(coords, coords))

        # Eliminate duplicate tuples (a,a), (b,b), etc.
        tuples = [t for t in tuples if t[0] != t[1]]

        for a, b in tuples:
            x_diff = b[0] - a[0]
            y_diff = b[1] - a[1]

            # >>> Part 1: Comment part 2 to enable part 1
            # Only consider one the antinodes before and behind. Compute the distance between the two frequencies
            # and calculate the antinodes before the first and behind the second frequency
            a_nodes = [
                (a[0] - x_diff, a[1] - y_diff),
                (b[0] + x_diff, b[1] + y_diff)
            ]
            # <<< END Part 1

            # >>> Part 2: Put the antinodes on the path between the two frequencies until the grid ends.
            # Comment part 1 to enable part 2
            grid_width = len(list_list[0])
            grid_height = len(list_list)
            a_nodes = []
            x_temp, y_temp = a
            while 0 <= x_temp < grid_width and 0 <= y_temp < grid_height:  # Antinodes before a
                x_temp -= x_diff
                y_temp -= y_diff
                a_nodes.append((x_temp, y_temp))

            x_temp, y_temp = b
            while 0 <= x_temp < grid_width and 0 <= y_temp < grid_height:  # Antinodes behind b
                x_temp += x_diff
                y_temp += y_diff
                a_nodes.append((x_temp, y_temp))

            a_nodes += [a, b]  # Include frequencies locations
            # <<< END Part 2

            for an in a_nodes:
                # Skip antinodes outside the grid
                if not (0 <= an[0] < grid_width and 0 <= an[1] < grid_height):
                    continue

                a_node_coords.add(an)  # Count it

                # Mark antinode with '#' on grid. Do not overwrite existing frequencies.
                marker_current = list_list[an[0]][an[1]]
                if marker_current not in frequency_coordinates.keys(): list_list[an[0]][an[1]] = "#"

    # Transpose list back to rows to print.
    list_list = list(map(list, zip(*list_list)))
    for line in list_list:
        print(''.join(line))

    print("Count: ", len(a_node_coords))


if __name__ == '__main__':
    part_1_and_2()  # Part1: 369 Part2: 1169
