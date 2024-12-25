#!/usr/bin/env python3

import sys
from functools import reduce

SAMPLES = [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3),
]


def parse_input(input):
    lines = [[c for c in line] for line in input.splitlines()]

    output = []
    for line in lines:
        output.extend(line)

    return output


def solution(input):
    moves = parse_input(input)

    return reduce(lambda sum, move: sum + 1 if move == "(" else sum - 1, moves, 0)


if __name__ == "__main__":
    for example, expected in SAMPLES:
        actual = solution(example)
        if actual != expected:
            print(f"❗Sample input incorrect; expected: {expected}, actual: {actual}")
            sys.exit(1)

    print("✅ Sample input passed")

    with open("input.txt", "r") as f:
        print(solution(f.read()))
