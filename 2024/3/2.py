#!/usr/bin/env python3

import re
import sys

SAMPLE_INPUT = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def read_mul_instructions(input):
    total = 0
    enabled = True

    for match in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", input):
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            x, y = re.findall(r"[0-9]{1,3}", match)

            if enabled:
                total += int(x) * int(y)

    return total


def driver():
    SAMPLE_EXPECTED = 48
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
