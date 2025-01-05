#!/usr/bin/env python3

import re
import sys
from dataclasses import dataclass
from enum import Enum

EXAMPLES = [
    ("turn on 0,0 through 0,0", 1),
    ("toggle 0,0 through 999,999", 2000000),
]


class Op(Enum):
    ON = 1
    TOGGLE = 2
    OFF = 3


@dataclass
class Instr:
    op: Op
    upper_left: tuple[int, int]
    bottom_right: tuple[int, int]


def parse_input(input):
    output = []
    for line in input.splitlines():
        match re.findall(r"^(turn on|toggle|turn off)", line)[0]:
            case "turn on":
                op = Op.ON
            case "toggle":
                op = Op.TOGGLE
            case "turn off":
                op = Op.OFF

        upper_left, bottom_right = [
            (int(a), int(b)) for a, b in re.findall("([0-9]+),([0-9]+)", line)
        ]

        output.append(Instr(op, upper_left, bottom_right))

    return output


def update_grid(grid: list[list[int]], instr: Instr):
    for y in range(instr.upper_left[0], instr.bottom_right[0] + 1):
        for x in range(instr.upper_left[1], instr.bottom_right[1] + 1):
            if instr.op == Op.ON:
                delta = 1
            elif instr.op == Op.OFF:
                delta = -1
            else:
                delta = 2

            grid[y][x] = max(grid[y][x] + delta, 0)


def solution(input):
    instrs = parse_input(input)

    grid = [[0] * 1000 for _ in range(1000)]

    for instr in instrs:
        update_grid(grid, instr)

    return sum([sum(row) for row in grid])


if __name__ == "__main__":
    for example, expected in EXAMPLES:
        actual = solution(example)
        if actual != expected:
            print(f"❗Example case failed; expected: {expected}, actual: {actual}")
            sys.exit(1)

    print("✅ Example cases passed")

    with open("input.txt", "r") as f:
        print(solution(f.read()))
