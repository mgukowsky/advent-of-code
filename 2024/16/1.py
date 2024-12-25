#!/usr/bin/env python3
from __future__ import annotations

import math
import sys
from collections import defaultdict
from dataclasses import dataclass

SAMPLE_INPUT = """\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ANGLES = [*zip(MOVES, MOVES[-1:] + MOVES[:-1])]


@dataclass
class Edge:
    weight: int
    to: tuple[int, int]


@dataclass
class Node:
    edges: list[Edge]


def parse_input(input):
    return [[c for c in line] for line in input.splitlines()]


def is_edge(grid, coord):
    if grid[coord[0]][coord[1]] == "#":
        return False

    paths = []

    for move in MOVES:
        new_coord = (coord[0] + move[0], coord[1] + move[1])
        if grid[new_coord[0]][new_coord[1]] == ".":
            paths.append(new_coord)

    if len(paths) < 2:
        return False
    # Not an edge b/c we're going straight through
    elif len(paths) == 2 and (paths[0][0] == paths[1][0] or paths[0][1] == paths[1][1]):
        return False
    else:
        return True


def get_extent(grid, coord, dir):
    extent = 0

    while True:
        new_coord = (coord[0] + dir[0], coord[1] + dir[1])
        if grid[new_coord[0]][new_coord[1]] == "#":
            break
        extent += 1
        coord = new_coord

    return extent


def record_edges(grid, coord, node_dict):
    if is_edge(grid, coord):
        for axis_a, axis_b in ANGLES:
            extent_a = get_extent(grid, coord, axis_a)
            extent_b = get_extent(grid, coord, axis_b)

            if extent_a > 0 and extent_b > 0:
                coord_a = (
                    coord[0] + (axis_a[0] * extent_a),
                    coord[1] + (axis_a[1] * extent_a),
                )
                coord_b = (
                    coord[0] + (axis_b[0] * extent_b),
                    coord[1] + (axis_b[1] * extent_b),
                )

                node_dict[coord_a].edges.append(
                    Edge(weight=1000 + extent_a + extent_b, to=coord_b)
                )
                node_dict[coord_b].edges.append(
                    Edge(weight=1000 + extent_a + extent_b, to=coord_a)
                )


def build_graph(grid):
    # Build a graph but allow for indexing by coord
    node_dict = defaultdict(lambda: Node(edges=[]))

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            record_edges(grid, (y, x), node_dict)

    return node_dict


def djikstra(grid, graph):
    unvisited = {k for k in graph.keys()}
    weights = {k: float("inf") for k in graph.keys()}

    # Start at the S node
    weights[(len(grid) - 2, 1)] = 0
    assert grid[len(grid) - 2][1] == "S"
    assert grid[1][len(grid[0]) - 2] == "E"

    while len(unvisited) > 0:
        node = min(unvisited, key=weights.get)

        # No reachable nodes left
        weight = weights[node]
        if math.isinf(weight):
            break

        for edge in graph[node].edges:
            weights[edge.to] = min(weight + edge.weight, weights[edge.to])

        unvisited.remove(node)

    print(weights)

    return weights[(1, len(grid[0]) - 2)]


def shortest_maze_path(input):
    grid = parse_input(input)
    graph = build_graph(grid)

    return djikstra(grid, graph)


def driver():
    SAMPLE_EXPECTED = 7036
    SAMPLE_ACTUAL = shortest_maze_path(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(shortest_maze_path(f.read()))


if __name__ == "__main__":
    driver()
