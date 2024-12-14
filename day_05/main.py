def read_input():
    with open("day_05/input.txt", "r") as file:
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


def part_1():
    """
    Approach:
    - Collect all rules in a dictionary. The key is the first number and the following number are put in a list.
    - For each line, check if the next number is in the list of the current number. If not, the line is incorrect.
    """
    sum_of_correct_lines = 0

    rules, lines = read_input()
    rules_dict = {}
    for rule in rules:
        if rule[0] in rules_dict:
            rules_dict[rule[0]].append(rule[1])
        else:
            rules_dict[rule[0]] = [rule[1]]

    for line in lines:
        is_correct_line = True
        for i in range(len(line) - 1):
            num_tail = rules_dict[line[i]]
            line_tail = line[i + 1:]

            for lt in line_tail:
                if lt not in num_tail:
                    is_correct_line = False
                    break

        if is_correct_line:
            index_mid = len(line) // 2
            sum_of_correct_lines += line[index_mid]

    print("Sum of all correct lines: ", sum_of_correct_lines)


if __name__ == '__main__':
    part_1()
