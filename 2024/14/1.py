#!/usr/bin/env python3

import re
import sys
from dataclasses import dataclass

import numpy as np


@dataclass
class Coord:
    x: int
    y: int


@dataclass
class RoboSpec:
    pos: Coord
    vel: Coord


SAMPLE_INPUT = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


def parse_input(input):
    output = []

    for line in input.splitlines():
        p, v = line.split(" ")
        pos = Coord(*[int(n) for n in re.findall(r"[0-9-]+", p)])
        vel = Coord(*[int(n) for n in re.findall(r"[0-9-]+", v)])
        output.append(RoboSpec(pos, vel))

    return output


def get_quadrant(mids, coord):
    if mids.x == coord.x or mids.y == coord.y:
        return -1
    elif coord.x < mids.x and coord.y < mids.y:
        return 0
    elif coord.x > mids.x and coord.y < mids.y:
        return 1
    elif coord.x > mids.x and coord.y > mids.y:
        return 2
    else:
        return 3


def get_safety_factor(input, dims):
    mids = Coord(int((dims.x - 1) / 2), int((dims.y - 1) / 2))
    print(mids)

    robo_specs = parse_input(input)
    quadrants = [0, 0, 0, 0]
    for spec in robo_specs:
        after = (spec.pos.x + (spec.vel.x * 100), spec.pos.y + (spec.vel.y * 100))
        adj_coord = Coord(x=after[0] % dims.x, y=after[1] % dims.y)
        quadrant = get_quadrant(mids, adj_coord)
        if quadrant > -1:
            quadrants[quadrant] += 1

    return np.array(quadrants).prod()


def driver():
    SAMPLE_EXPECTED = 12
    SAMPLE_ACTUAL = get_safety_factor(SAMPLE_INPUT, Coord(11, 7))
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(get_safety_factor(f.read(), Coord(101, 103)))


if __name__ == "__main__":
    driver()
