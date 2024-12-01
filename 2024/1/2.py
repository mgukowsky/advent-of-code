#!/usr/bin/env python3

import sys
from collections import Counter

SAMPLE_INPUT_1 = """\
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


def puzzle_2_1(input: str):
    nums, freq_list = transform_input(input)

    freq_dict = Counter(freq_list)

    return sum([n * freq_dict[n] for n in nums])


def driver():
    SAMPLE_EXPECTED = 31
    SAMPLE_ACTUAL = puzzle_2_1(SAMPLE_INPUT_1)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(puzzle_2_1(f.read()))


if __name__ == "__main__":
    driver()
