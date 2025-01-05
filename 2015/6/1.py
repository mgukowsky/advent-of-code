#!/usr/bin/env python3

import re
import sys
from dataclasses import dataclass
from enum import Enum
from itertools import pairwise, starmap

EXAMPLES = [
    ("turn on 0,0 through 999,999", 1000000),
    ("toggle 0,0 through 999,0", 1000),
    ("turn off 499,499 through 500,500", 0),
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
                grid[y][x] = True
            elif instr.op == Op.OFF:
                grid[y][x] = False
            else:
                grid[y][x] = not grid[y][x]


def solution(input):
    instrs = parse_input(input)

    grid = [[False] * 1000 for _ in range(1000)]

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
