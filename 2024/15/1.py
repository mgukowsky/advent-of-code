#!/usr/bin/env python3

import sys

SAMPLE_INPUT = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""


def parse_input(input):
    grid = []
    moves = []

    parsing_grid = True

    for line in input.splitlines():
        if len(line) == 0:
            parsing_grid = False
        elif parsing_grid:
            grid.append([c for c in line])
        else:
            for move in [m for m in line]:
                match move:
                    case "<":
                        moves.append((0, -1))
                    case "^":
                        moves.append((-1, 0))
                    case ">":
                        moves.append((0, 1))
                    case "v":
                        moves.append((1, 0))

    return (grid, moves)


def is_valid_space(coord, grid):
    return (
        coord[0] > -1
        and coord[0] < len(grid)
        and coord[1] > -1
        and coord[1] < len(grid[0])
    )


def get_robot_coord(grid):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "@":
                return (y, x)


def try_move(grid, coord, move):
    new_coord = (coord[0] + move[0], coord[1] + move[1])

    if (not is_valid_space(new_coord, grid)) or grid[new_coord[0]][new_coord[1]] == "#":
        return False
    elif grid[new_coord[0]][new_coord[1]] == "O":
        return try_move(grid, new_coord, move)
    else:
        grid[new_coord[0]][new_coord[1]] = "O"
        return True


def move_boxes(input):
    grid, moves = parse_input(input)

    robot_coord = get_robot_coord(grid)

    for move in moves:
        if try_move(grid, robot_coord, move):
            new_coord = (robot_coord[0] + move[0], robot_coord[1] + move[1])
            grid[robot_coord[0]][robot_coord[1]] = "."
            grid[new_coord[0]][new_coord[1]] = "@"
            robot_coord = new_coord

    sum = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if grid[y][x] == "O":
                sum += (100 * y) + x

    return sum


def driver():
    SAMPLE_EXPECTED = 10092
    SAMPLE_ACTUAL = move_boxes(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(move_boxes(f.read()))


if __name__ == "__main__":
    driver()
