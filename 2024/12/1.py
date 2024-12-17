#!/usr/bin/env python3


import sys

SAMPLE_INPUT = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
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
    return [[val for val in line] for line in input.splitlines()]


def get_area_x_permimeter(grid, coord, plant_type, visited):
    if coord in visited:
        return 0

    plants_to_visit = [coord]
    visited.add(coord)

    area = 0
    perimeter = 0
    while len(plants_to_visit) > 0:
        plant = plants_to_visit.pop(0)
        area += 1

        for move in MOVES:
            next_plant = (plant[0] + move[0], plant[1] + move[1])
            if (not is_valid_space(next_plant, grid)) or grid[next_plant[0]][
                next_plant[1]
            ] != plant_type:
                perimeter += 1
            elif next_plant not in visited:
                plants_to_visit.append(next_plant)
                visited.add(next_plant)

    return area * perimeter


def fence_price(input):
    grid = parse_input(input)

    visited = set()
    sum = 0

    for y, row in enumerate(grid):
        for x, plant in enumerate(row):
            sum += get_area_x_permimeter(grid, (y, x), plant, visited)

    return sum


def driver():
    SAMPLE_EXPECTED = 1930
    SAMPLE_ACTUAL = fence_price(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(fence_price(f.read()))


if __name__ == "__main__":
    driver()
