#!/usr/bin/env python3

import re
import sys
from functools import reduce
from itertools import combinations
from operator import mul

EXAMPLES = [
    ("2x3x4", 34),
    ("1x1x10", 14),
]


def parse_input(input):
    return [
        [int(n) for n in re.findall(r"[0-9]+", line)] for line in input.splitlines()
    ]


def solution(input):
    boxes = parse_input(input)

    sum = 0
    for box in boxes:
        bow_ribbon = reduce(lambda x, y: x * y, box, 1)
        minside_x, minside_y = min(combinations(box, 2), key=lambda side: mul(*side))
        box_ribbon = minside_x * 2 + minside_y * 2
        sum = sum + box_ribbon + bow_ribbon

    return sum


if __name__ == "__main__":
    for example, expected in EXAMPLES:
        actual = solution(example)
        if actual != expected:
            print(f"❗Example case failed; expected: {expected}, actual: {actual}")
            sys.exit(1)

    print("✅ Example cases passed")

    with open("input.txt", "r") as f:
        print(solution(f.read()))
