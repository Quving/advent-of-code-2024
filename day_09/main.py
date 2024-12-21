#!/usr/bin/env python3
""" Day 09 - Advent of Code 2024 """


def read_input(test: bool = False) -> str:
    """
    Read input from file and return as a list of integers
    :return:
    """
    filename = f"day_09/input{"_test" if test else ""}.txt"
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()


def compute_checksum(disk_map: list[list[str]]) -> int:
    """
    Compute the checksum of the disk map
    :param disk_map:
    :return:
    """
    return sum([i * int(block[0]) for i, block in enumerate(disk_map) if '.' not in block])


def decipher_disk_map(disk_map: list[str]) -> list[list[str]]:
    disk_map_deciphered = []
    for i, block in enumerate(disk_map):
        is_file = i % 2 == 0

        if is_file:
            element = [[str(i // 2)] for _ in range(int(block))]
        else:
            element = [['.'] for _ in range(int(block))]

        disk_map_deciphered.extend(element)

    return disk_map_deciphered


def defragment_disk_map(disk_map: list[list[str]]):
    """
    Defragment the disk map
    :param disk_map:
    :return:
    """
    disk_map_copy = [x.copy() for x in disk_map]
    for i, block in enumerate(disk_map_copy):
        if block != ['.']:
            continue

        # print("".join(disk_map))
        for j in range(i, len(disk_map_copy)):
            j_reverse = len(disk_map_copy) - (j - i) - 1
            if disk_map_copy[j_reverse] != ['.']:
                disk_map_copy[i], disk_map_copy[j_reverse] = disk_map_copy[j_reverse], disk_map_copy[i]  # Swap blocks
                break  # Cancel the loop after the first swap

    return disk_map_copy


def part_1():
    """
    Part 1
    :return:
    """
    disk_map = list(read_input(test=False))  # list[str]

    disk_map = decipher_disk_map(disk_map)
    disk_map = defragment_disk_map(disk_map)

    print("Checksum: ", compute_checksum(disk_map))


if __name__ == '__main__':
    part_1()  # Not: 88881734731 (too low)
    # part_2()
    # print(decipher_disk_map(list("2333133121414131402")) == '00...111...2...333.44.5555.6666.777.888899')
