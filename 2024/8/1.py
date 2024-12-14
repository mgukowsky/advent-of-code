#!/usr/bin/env python3


import sys
from itertools import combinations, permutations

SAMPLE_INPUT = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def is_valid_space(coord, grid):
    return (
        coord[0] > -1
        and coord[0] < len(grid)
        and coord[1] > -1
        and coord[1] < len(grid[0])
    )


def parse_input(input):
    return [[val for val in line] for line in input.splitlines()]


def make_node_dict(grid):
    node_dict = {}

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val != ".":
                coord = (y, x)
                if val not in node_dict:
                    node_dict[val] = [coord]
                else:
                    node_dict[val].append(coord)

    return node_dict


def get_num_antinodes(grid, coord1, coord2):
    valid_antinodes = []
    for lhs, rhs in permutations([coord1, coord2]):
        # Get the distance vector from a to b, then double it
        vec = ((rhs[0] - lhs[0]) * 2, (rhs[1] - lhs[1]) * 2)
        potential_antinode = (lhs[0] + vec[0], lhs[1] + vec[1])
        if is_valid_space(potential_antinode, grid):
            valid_antinodes.append(potential_antinode)

    return valid_antinodes


def sum_antinodes(input):
    grid = parse_input(input)
    node_dict = make_node_dict(grid)

    antinodes = set()
    for _, coords in node_dict.items():
        for combi in combinations(coords, 2):
            antinodes.update(get_num_antinodes(grid, *combi))

    return len(antinodes)


def driver():
    SAMPLE_EXPECTED = 14
    SAMPLE_ACTUAL = sum_antinodes(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(sum_antinodes(f.read()))


if __name__ == "__main__":
    driver()