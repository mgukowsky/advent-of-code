#!/usr/bin/env python3

SAMPLE_INPUT_1_1 = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


def transform_input(input: str):
    list1 = []
    list2 = []

    for entry in input.splitlines():
        first, second = entry.split()
        list1.append(int(first))
        list2.append(int(second))

    return [list1, list2]


def puzzle_1_1(input: str):
    list1, list2 = transform_input(input)
    list1.sort()
    list2.sort()

    return sum([abs(a - b) for a, b in zip(list1, list2)])


if __name__ == "__main__":
    SAMPLE_EXPECTED = 11
    SAMPLE_ACTUAL = puzzle_1_1(SAMPLE_INPUT_1_1)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

    with open("input.txt", "r") as f:
        print(puzzle_1_1(f.read()))
