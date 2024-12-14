#!/usr/bin/env python3


import sys

SAMPLE_INPUT = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_valid_space(coord, grid):
    return (
        coord[0] > -1
        and coord[0] < len(grid)
        and coord[1] > -1
        and coord[1] < len(grid[0])
    )


def parse_input(input):
    return [[int(val) for val in line] for line in input.splitlines()]


# Only difference is that we now want to account for all possible paths, so we just have to remove our cache of seen summits
def evaluate_trailhead(grid, coord):
    level = grid[coord[0]][coord[1]]

    if level == 9:
        return 1

    sum = 0

    for move in MOVES:
        new_coord = (coord[0] + move[0], coord[1] + move[1])
        if (
            is_valid_space(new_coord, grid)
            and grid[new_coord[0]][new_coord[1]] == level + 1
        ):
            sum += evaluate_trailhead(grid, new_coord)

    return sum


def sum_trailheads(input):
    grid = parse_input(input)
    sum = 0

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == 0:
                sum += evaluate_trailhead(grid, (y, x))

    return sum


def driver():
    SAMPLE_EXPECTED = 81
    SAMPLE_ACTUAL = sum_trailheads(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(sum_trailheads(f.read()))


if __name__ == "__main__":
    driver()
