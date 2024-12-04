#!/usr/bin/env python3

import sys
from itertools import pairwise

SAMPLE_INPUT_1_1 = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def transform_input(input: str):
    return [[int(num) for num in line.split()] for line in input.splitlines()]


def sign(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1


def is_row_safe(row):
    if len(row) < 2:
        return True

    direction = sign(row[0] - row[1])

    for lhs, rhs in pairwise(row):
        diff = lhs - rhs

        if diff == 0 or abs(diff) > 3 or sign(diff) != direction:
            return False

    return True


def puzzle_1_1(input: str):
    reports = transform_input(input)

    return sum(int(is_row_safe(row)) for row in reports)


def driver():
    SAMPLE_EXPECTED = 2
    SAMPLE_ACTUAL = puzzle_1_1(SAMPLE_INPUT_1_1)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(puzzle_1_1(f.read()))


if __name__ == "__main__":
    driver()
