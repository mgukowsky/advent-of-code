#!/usr/bin/env python3


from functools import cache

SAMPLE_INPUT = """\
125 17
"""


def parse_input(input):
    return [int(n) for n in input.split(" ")]


# Key realization is that we just care about returning the length, and therefore we can memoize subproblems.
# Inspired by https://www.reddit.com/r/adventofcode/comments/1hbm0al/comment/m1xt7uu/
@cache
def do_blink(stone, iterations):
    for i in range(iterations):
        if stone == 0:
            stone = 1
        else:
            stonestr = str(stone)
            if len(stonestr) % 2 == 0:
                midpoint = int(len(stonestr) / 2)
                return do_blink(
                    int(stonestr[:midpoint]), iterations - (i + 1)
                ) + do_blink(int(stonestr[midpoint:]), iterations - (i + 1))
            else:
                stone *= 2024

    return 1


def blink_stones(input):
    stones = parse_input(input)
    return sum(do_blink(stone, 75) for stone in stones)


def driver():
    with open("input.txt", "r") as f:
        print(blink_stones(f.read()))


if __name__ == "__main__":
    driver()
