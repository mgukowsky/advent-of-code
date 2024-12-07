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

    guard_vec = (-1, 0)

    guard_pos = (guard_pos[0], guard_pos[1], guard_vec)
    visited_spaces = [guard_pos]

    while True:
        next_pos = (guard_pos[0] + guard_vec[0], guard_pos[1] + guard_vec[1], guard_vec)

        if not is_valid_space(next_pos, grid):
            break
        elif grid[next_pos[0]][next_pos[1]] == "#":
            while True:
                guard_pos = (guard_pos[0], guard_pos[1], rotate_90(guard_pos[2]))
                guard_vec = guard_pos[2]

                if (
                    grid[guard_pos[0] + guard_vec[0]][guard_pos[1] + guard_vec[1]]
                    != "#"
                ):
                    break
        else:
            guard_pos = next_pos
            visited_spaces.append(guard_pos)

    return visited_spaces


def is_loop(space, visited_spaces, grid):

    guard_pos = visited_spaces[-1]
    guard_pos = (guard_pos[0], guard_pos[1], rotate_90(guard_pos[2]))
    guard_vec = guard_pos[2]
    # print("--------")
    # print(space)
    # for sp in visited_spaces:
    #     print(sp)
    visited_spaces_set = set(visited_spaces)

    while True:
        next_pos = (guard_pos[0] + guard_vec[0], guard_pos[1] + guard_vec[1], guard_vec)
        # print(f"np: {next_pos}")

        if not is_valid_space(next_pos, grid):
            # print("FALSE")
            return False
        elif grid[next_pos[0]][next_pos[1]] == "#":
            while True:
                guard_pos = (guard_pos[0], guard_pos[1], rotate_90(guard_pos[2]))
                guard_vec = guard_pos[2]

                if (
                    grid[guard_pos[0] + guard_vec[0]][guard_pos[1] + guard_vec[1]]
                    != "#"
                ):
                    break
        else:
            guard_pos = next_pos

        if guard_pos in visited_spaces_set:
            # print(f"p: {guard_pos}")
            # for space in visited_spaces_set:
            #     print(space)
            # print("TRUE")
            return True

        visited_spaces_set.add(guard_pos)


def get_num_loop_spaces(input):
    visited_spaces = walk_map(input)
    grid, _ = parse_input(input)

    sum = 0

    while len(visited_spaces) > 1:
        space = visited_spaces.pop()
        grid[space[0]][space[1]] = "#"
        sum += int(is_loop(space, list(visited_spaces), grid))
        grid[space[0]][space[1]] = "."

    return sum


def driver():
    SAMPLE_EXPECTED = 6
    SAMPLE_ACTUAL = get_num_loop_spaces(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(get_num_loop_spaces(f.read()))


if __name__ == "__main__":
    driver()
