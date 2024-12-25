#!/usr/bin/env python3

import sys

EXAMPLES = [
    (")", 1),
    ("()())", 5),
]


def parse_input(input):
    lines = [[c for c in line] for line in input.splitlines()]

    output = []
    for line in lines:
        output.extend(line)

    return output


def solution(input):
    moves = parse_input(input)

    current_floor = 0
    for idx, move in enumerate(moves):
        current_floor = current_floor + 1 if move == "(" else current_floor - 1

        if current_floor == -1:
            return idx + 1


if __name__ == "__main__":
    for example, expected in EXAMPLES:
        actual = solution(example)
        if actual != expected:
            print(f"❗Example case failed; expected: {expected}, actual: {actual}")
            sys.exit(1)

    print("✅ Example cases passed")

    with open("input.txt", "r") as f:
        print(solution(f.read()))
