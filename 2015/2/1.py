#!/usr/bin/env python3

import re
import sys
from itertools import combinations

EXAMPLES = [
    ("2x3x4", 58),
    ("1x1x10", 43),
]


def parse_input(input):
    return [
        [int(n) for n in re.findall(r"[0-9]+", line)] for line in input.splitlines()
    ]


def solution(input):
    boxes = parse_input(input)

    sum = 0
    for box in boxes:
        w, h, l = tuple(box)
        area = 2 * l * w + 2 * w * h + 2 * h * l
        minside = min([x * y for x, y in combinations(box, 2)])
        sum = sum + area + minside

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
