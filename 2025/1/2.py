#!/usr/bin/env python3

import operator
import re
import sys

SAMPLE_INPUTS = [
    (
        """\
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
""",
        6,
    ),
    (
        """\
R1000
""",
        10,
    ),
    (
        """\
L1000
""",
        10,
    ),
]


def parse_input(input):
    output = []

    for line in input.splitlines():
        n = int(line[1:])
        output.append(n if line[0] == "R" else n * -1)

    return output


def rotation_password(input):
    password = 0
    dial = 50

    for n in parse_input(input):
        clicks_past_100 = abs(n) // 100
        password += clicks_past_100

        rem_clicks = (
            n - (100 * clicks_past_100) if n >= 0 else n + (100 * clicks_past_100)
        )
        if abs(rem_clicks) > 0:
            before_dial = dial
            dial = dial + rem_clicks
            if before_dial != 0 and (dial < 0 or dial > 100):
                password += 1
            dial = dial % 100
            if dial == 0:
                password += 1

    return password


def driver():
    for input, expected in SAMPLE_INPUTS:
        actual = rotation_password(input)
        if expected == actual:
            print("✅ Sample input passed")
        else:
            print(f"❗Sample input incorrect; expected: {expected}, actual: {actual}")

            sys.exit(1)

    with open("input.txt", "r") as f:
        print(rotation_password(f.read()))


if __name__ == "__main__":
    driver()
