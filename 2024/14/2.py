#!/usr/bin/env python3

import re
import time
from dataclasses import dataclass


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


def render_grid(input, dims, secs):
    robo_specs = parse_input(input)
    grid = [[0 for x in range(dims.x)] for y in range(dims.y)]
    for spec in robo_specs:
        after = (spec.pos.x + (spec.vel.x * secs), spec.pos.y + (spec.vel.y * secs))
        adj_coord = Coord(x=after[0] % dims.x, y=after[1] % dims.y)
        grid[adj_coord.y][adj_coord.x] += 1
        if grid[adj_coord.y][adj_coord.x] > 1:
            return False

    for row in grid:
        print("".join([str(el) if el > 0 else "." for el in row]))

    return True


# Based on this assumption that no robots would be overlapping in the solution: https://www.reddit.com/r/adventofcode/comments/1hdvhvu/comment/m20p2sh/
# Much cooler solutions in that thread!
def driver():
    with open("input.txt", "r") as f:
        i = 1
        input = f.read()
        while True:
            shown = render_grid(input, Coord(101, 103), i)
            if shown:
                print(f"Iter: {i}\n\n")
                time.sleep(1)

            i += 1


if __name__ == "__main__":
    driver()
