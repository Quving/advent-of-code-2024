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
        elif operators[i - 1] == '||':
            result = int(str(result) + str(elements[i]))
        else:
            raise ValueError("Invalid operator")

    return result


def symbol_counter(symbols: list, n: int):
    """
    Given a list of symbols and a number n, generate all numbers with base n. Like binary, ternary, etc.
    :param symbols:
    :param n:
    :return:
    """

    def to_number_with_base(x, base):
        if x == 0:
            return '0'

        result = []
        while x:
            x, r = divmod(x, base)
            result.append(str(r))

        return ''.join(reversed(result))

    # Generate all numbers with base n
    numbers_str = []
    for i in range(n):
        number = to_number_with_base(i, len(symbols))

        # Add leading zeros
        numbers_str.append(number.zfill(len(to_number_with_base(n - 1, len(symbols)))))

    # Replace numbers with symbols
    numbers_list = []
    for i, number in enumerate(numbers_str):
        numbers_list.append([symbols[int(n)] for n in number])

    return numbers_list


def part_1():
    """
    The approach is to brute force all combinations of operators and check if the result is correct. Use a counter
    with a associated base to generate all combinations.
    :return:
    """
    equations = read_input()

    correct_equations_count = 0
    sum_test_values = 0

    for eq in equations:
        result, parts = eq
        op_combinations = symbol_counter(['+', '*'], 2 ** (len(parts) - 1))

        # Brute force all combinations
        for op_combination in op_combinations:
            if compute_result(parts, op_combination) == result:
                correct_equations_count += 1
                sum_test_values += result
                break

    print("Correct equations: ", correct_equations_count)
    print("Sum of test values: ", sum_test_values)


def part_2():
    """
    The approach is the same as in part 1, but we need to add the concatenation operator '||'.
    :return:
    """
    equations = read_input()

    correct_equations_count = 0
    sum_test_values = 0

    for eq in equations:
        result, parts = eq
        # We want elements of length len(part)-1, so we need to count until 3 ** (len(parts) - 1)
        op_combinations = symbol_counter(['+', '*', '||'], 3 ** (len(parts) - 1))

        # Brute force all combinations
        for op_combination in op_combinations:
            if compute_result(parts, op_combination) == result:
                correct_equations_count += 1
                sum_test_values += result
                break

    print("Correct equations: ", correct_equations_count)
    print("Sum of test values: ", sum_test_values)


if __name__ == '__main__':
    print(symbol_counter(['!', '?'], 8))
    part_1()  # Result: 1582598718861
    part_2()  # Result:  165278151522644
