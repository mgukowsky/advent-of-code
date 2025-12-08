#!/usr/bin/env python3

import operator
import re
import sys

SAMPLE_INPUT = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def parse_input(input):
    output = []

    for line in input.splitlines():
        n = int(line[1:])
        output.append(n if line[0] == "L" else n * -1)

    return output


def rotation_password(input):
    password = 0
    dial = 50

    for n in parse_input(input):
        dial = (dial + n) % 100
        if dial == 0:
            password += 1

    return password


def driver():
    SAMPLE_EXPECTED = 3
    SAMPLE_ACTUAL = rotation_password(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(rotation_password(f.read()))


if __name__ == "__main__":
    driver()
