#!/usr/bin/env python3
""" Day 07 - Advent of Code 2024 """


def read_input() -> list[tuple]:
    with open("day_07/input.txt", "r", encoding='utf-8') as file:
        equations = []
        for line in file:
            result, parts = line.strip().split(":")

            parts = [int(part) for part in parts.split()]
            result = int(result)

            equations.append((result, parts))

        return equations


def get_all_combinations(n: int) -> list:
    """
    Get all possible combinations of operators for a given length of elements
    :param n:
    :param elements:
    :return:
    """

    # Count to n binary.
    binary_counts = []
    for i in range(2 ** n):
        binary_counts.append(bin(i)[2:].zfill(len(bin(2 ** n - 1)[2:])))

    # Replace 0 with + and 1 with *
    all_combinations = []
    for binary_count in binary_counts:
        combination = []
        for b in binary_count:
            if b == '0':
                combination.append('+')
            elif b == '1':
                combination.append('*')
            else:
                raise ValueError("Invalid binary count")

        all_combinations.append(combination)
    return all_combinations


def compute_result(elements: list, operators: list):
    """
    Compute the result of the elements and operators from left to right. Without precedence.
    :param elements:
    :param operators:
    :return:
    """
    if len(elements) - 1 != len(operators):
        raise ValueError("Number of elements and operators do not match")

    result = elements[0]
    for i in range(1, len(elements)):
        if operators[i - 1] == '+':
            result += elements[i]
        elif operators[i - 1] == '*':
            result *= elements[i]
        else:
            raise ValueError("Invalid operator")

    return result


def part_1():
    equations = read_input()

    correct_equations_count = 0
    sum_test_values = 0

    for eq in equations:
        result, parts = eq
        op_combinations = get_all_combinations(n=len(parts) - 1)

        # Brute force all combinations
        for op_combination in op_combinations:
            if compute_result(parts, op_combination) == result:
                correct_equations_count += 1
                sum_test_values += result
                break

    print("Correct equations: ", correct_equations_count)
    print("Sum of test values: ", sum_test_values)


if __name__ == '__main__':
    part_1()
