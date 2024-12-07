#!/usr/bin/env python3

import sys

SAMPLE_INPUT = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def is_valid_space(coord, grid):
    return (
        coord[0] > -1
        and coord[0] < len(grid)
        and coord[1] > -1
        and coord[1] < len(grid[0])
    )


def rotate_90(vec):
    match (vec):
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)


def parse_input(input):
    output = []
    guard_coord = None

    for y, line in enumerate(input.splitlines()):
        spaces = [c for c in line]
        output.append(spaces)

        for x, space in enumerate(spaces):
            if space == "^":
                guard_coord = (y, x)

    return (output, guard_coord)


def walk_map(input):
    grid, guard_pos = parse_input(input)

    visited_spaces = set()
    guard_vec = (-1, 0)

    while True:
        visited_spaces.add(guard_pos)

        next_pos = (guard_pos[0] + guard_vec[0], guard_pos[1] + guard_vec[1])

        if not is_valid_space(next_pos, grid):
            break
        elif grid[next_pos[0]][next_pos[1]] == "#":
            guard_vec = rotate_90(guard_vec)
        else:
            guard_pos = next_pos

    return len(visited_spaces)


def driver():
    SAMPLE_EXPECTED = 41
    SAMPLE_ACTUAL = walk_map(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(walk_map(f.read()))


if __name__ == "__main__":
    driver()
