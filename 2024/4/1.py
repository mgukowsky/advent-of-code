#!/usr/bin/env python3

import sys
from itertools import permutations

SAMPLE_INPUT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

MOVES = [(1, 1), (-1, -1), *permutations([-1, 0, 1])]


def get_next_letter(frag):
    match frag:
        case "X":
            return "M"
        case "XM":
            return "A"
        case "XMA":
            return "S"
        case _:
            raise RuntimeError(f"Invalid fragment: {frag}")


def is_legal_move(coord, dims):
    return coord[0] > -1 and coord[0] < dims[0] and coord[1] > -1 and coord[1] < dims[1]


def exhaustive_search(
    cache: set, current_coord: tuple, coord_set: set, frag: str, grid, direction
):
    if frag == "XMAS":
        # sets can't be hashed, but frozensets can be
        cache.add(frozenset(coord_set))
    else:
        next_letter = get_next_letter(frag)

        # If we are on the first letter, we have to search in all 8 directions.
        # But if we already have a direction, then we can only continue along that vector.
        moves = MOVES if direction is None else [direction]

        for move in moves:
            new_coord = (current_coord[0] + move[0], current_coord[1] + move[1])

            if (
                is_legal_move(new_coord, (len(grid), len(grid[0])))
                and grid[new_coord[0]][new_coord[1]] == next_letter
            ):
                exhaustive_search(
                    cache,
                    new_coord,
                    set([*coord_set, new_coord]),
                    frag + next_letter,
                    grid,
                    move,
                )


def xmas_search(input):
    grid = [[char for char in line] for line in input.splitlines()]

    # Record "XMAS" coords in a set to handle duplicates during our search
    cache = set()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "X":
                exhaustive_search(cache, (y, x), set([(y, x)]), "X", grid, None)

    return len(cache)


def driver():
    SAMPLE_EXPECTED = 18
    SAMPLE_ACTUAL = xmas_search(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(xmas_search(f.read()))


if __name__ == "__main__":
    driver()
