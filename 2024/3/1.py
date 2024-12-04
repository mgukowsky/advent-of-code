#!/usr/bin/env python3

import re
import sys

SAMPLE_INPUT = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""


def read_mul_instructions(input):
    total = 0

    for match in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input):
        x, y = re.findall(r"[0-9]{1,3}", match)
        total += int(x) * int(y)

    return total


def driver():
    SAMPLE_EXPECTED = 161
    SAMPLE_ACTUAL = read_mul_instructions(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(read_mul_instructions(f.read()))


if __name__ == "__main__":
    driver()
