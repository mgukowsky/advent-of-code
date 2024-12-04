#!/usr/bin/env python3

import sys
from collections import Counter
from itertools import pairwise

SAMPLE_INPUT_2_2 = """\
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

    adjusted = False

    # Evaluate the directions that the row moves in
    signs = [sign(lhs - rhs) for lhs, rhs in pairwise(row)]
    sign_freq = Counter(signs)

    # If there are multiple duplicate values and a change in direction, then the row cannot be made safe
    if len(sign_freq) > 2:
        return False

    # There is at least one change in direction
    if len(sign_freq) == 2:

        min_change, min_change_freq = sorted(sign_freq.items(), key=lambda kv: kv[1])[0]

        # If there is more than one change in direction, then the row cannot be made safe
        if min_change_freq != 1:
            return False

        # Otherwise, let's drop the offending value, which will be at the row index where the sign change occurs.
        # N.B. there is an edge case where the last value will not be detected if it is the valid
        # value to drop (e.g. [1,2,3,4,99]), but this is addressed after this block
        else:
            del row[signs.index(min_change)]
            adjusted = True

    deltas = [abs(lhs - rhs) for lhs, rhs in pairwise(row)]

    # If there is more than one place where the difference between adjacent numbers is invalid, then the row cannot be safe
    print(f"deltas: {deltas}")
    print(f"cdeltas: {Counter([*map(lambda n: 0 < n < 4, deltas)])}")
    num_unsafe_steps = Counter([*map(lambda n: 0 < n < 4, deltas)])[False]

    if num_unsafe_steps == 1 and (
        ((deltas[0] > 3 or deltas[0] < 1) or (deltas[-1] > 3 or deltas[-1] < 1))
        and not adjusted
    ):
        return True

    if num_unsafe_steps > 0:
        return False

    return True


def puzzle_2_2(input: str):
    reports = transform_input(input)

    return sum(int(is_row_safe(row)) for row in reports)


def driver():
    SAMPLE_EXPECTED = 4
    SAMPLE_ACTUAL = puzzle_2_2(SAMPLE_INPUT_2_2)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(puzzle_2_2(f.read()))


if __name__ == "__main__":
    driver()
