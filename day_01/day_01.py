def get_input() -> tuple:
    list_1 = []
    list_2 = []

    with open('day-01/input.txt') as f:
        for line in f:
            element_a, element_b = line.strip().split()
            list_1.append(int(element_a))
            list_2.append(int(element_b))

    return list_1, list_2


def part_1():
    column_a, column_b = get_input()

    column_a.sort()
    column_b.sort()

    diff_sum = 0
    for a, b in zip(column_a, column_b):
        diff_sum += abs(a - b)

    print("Total sum of differences: ", diff_sum)


def part_2():
    column_a, column_b = get_input()

    count_elements = {}
    for element in column_b:
        if element in count_elements:
            count_elements[element] += 1
        else:
            count_elements[element] = 1

    similarity_score = 0
    for element_a in column_a:
        similarity_score += element_a * count_elements.get(element_a, 0)

    print("Total similarity score: ", similarity_score)


if __name__ == '__main__':
    part_1()
    part_2()
