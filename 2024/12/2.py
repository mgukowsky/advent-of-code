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


# Evaluate an edge that lies between `coord` and `coord + move` to see if it is a new side, extends
# an existing side, or combining two sides together.
def evaluate_edge(grid, coord, move, edge_map_x, edge_map_y):
    # If we are changing the y coordinate, then the edge lies on the x axis
    is_x_edge = move in [(1, 0), (-1, 0)]

    # We map one element of the coordinate to a set of the other elements that we've seen
    # For example, a straight line [0, 0], [0, 1], [0, 2] would reduce to {0: [0,1,2]}
    edge_map = edge_map_y if is_x_edge else edge_map_x
    edge_key = coord[0] if is_x_edge else coord[1]
    edge_val = coord[1] if is_x_edge else coord[0]

    if edge_key not in edge_map:
        edge_map[edge_key] = set([(edge_val, move)])
    else:
        edge_map[edge_key].add((edge_val, move))

    # Get the two possibly adjacent edges
    l_edge = (edge_val - 1, move)
    r_edge = (edge_val + 1, move)

    # We are connecting two edges, which means that two separate edges are being combined into one side
    if (l_edge in edge_map[edge_key]) and (r_edge in edge_map[edge_key]):
        return -1

    # We are connecting to another edge, which means that we are extending a side
    elif (l_edge in edge_map[edge_key]) or (r_edge in edge_map[edge_key]):
        return 0

    # We have found a new side
    else:
        return 1


def get_area_x_sides(grid, coord, plant_type, visited):
    if coord in visited:
        return 0

    plants_to_visit = [coord]
    visited.add(coord)

    area = 0
    edge_map_x = {}
    edge_map_y = {}
    sides = 0
    while len(plants_to_visit) > 0:
        plant = plants_to_visit.pop(0)
        area += 1

        for move in MOVES:
            next_plant = (plant[0] + move[0], plant[1] + move[1])
            if (not is_valid_space(next_plant, grid)) or grid[next_plant[0]][
                next_plant[1]
            ] != plant_type:
                sides += evaluate_edge(grid, plant, move, edge_map_x, edge_map_y)
            elif next_plant not in visited:
                plants_to_visit.append(next_plant)
                visited.add(next_plant)

    return area * sides


def fence_price(input):
    grid = parse_input(input)

    visited = set()
    sum = 0

    for y, row in enumerate(grid):
        for x, plant in enumerate(row):
            sum += get_area_x_sides(grid, (y, x), plant, visited)

    return sum


def driver():
    SAMPLE_EXPECTED = 1206
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
