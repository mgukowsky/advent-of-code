#!/usr/bin/env python3

import sys
from collections import Counter

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

MOVES = [(1, 1), (-1, 1), (-1, -1), (1, -1)]


def is_legal_move(coord, dims):
    return coord[0] > -1 and coord[0] < dims[0] and coord[1] > -1 and coord[1] < dims[1]


def check_mas_x(cache, coord, grid):
    surrounding_letters = []
    m_coords = []
    coord_set = set([coord])

    for move in MOVES:
        new_coord = (coord[0] + move[0], coord[1] + move[1])

        if not is_legal_move(new_coord, (len(grid), len(grid[0]))):
            return

        new_letter = grid[new_coord[0]][new_coord[1]]

        if new_letter not in ["S", "M"]:
            return

        surrounding_letters.append(new_letter)
        coord_set.add(new_coord)

        if new_letter == "M":
            m_coords.append(new_coord)

    letter_freq = Counter(surrounding_letters)

    if len(m_coords) != 2:
        return

    # We need to address the corner case where a "SAS" crosses with a "MAM"
    #   S . M
    #   . A .
    #   M . S
    if not (m_coords[0][0] == m_coords[1][0] or m_coords[0][1] == m_coords[1][1]):
        return

    if letter_freq["M"] == 2 and letter_freq["S"] == 2:
        cache.add(frozenset(coord_set))


def mas_x_search(input):
    grid = [[char for char in line] for line in input.splitlines()]

    # Record "MAS"-x shape coords in a set to handle duplicates during our search
    cache = set()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "A":
                check_mas_x(cache, (y, x), grid)

    return len(cache)


def driver():
    SAMPLE_EXPECTED = 9
    SAMPLE_ACTUAL = mas_x_search(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(mas_x_search(f.read()))


if __name__ == "__main__":
    driver()
