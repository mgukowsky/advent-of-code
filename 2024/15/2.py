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


def double_grid(grid):
    new_grid = []

    for row in grid:
        new_row = []
        for char in row:
            match char:
                case "#":
                    new_row.extend(["#"] * 2)
                case "O":
                    new_row.extend(["[", "]"])
                case ".":
                    new_row.extend(["."] * 2)
                case "@":
                    new_row.extend(["@", "."])
        new_grid.append(new_row)

    return new_grid


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

    return (double_grid(grid), moves)


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


def move_forward(grid, coords, new_coords):
    assert len(coords) == len(new_coords)

    for coord, new_coord in zip(coords, new_coords):
        grid[new_coord[0]][new_coord[1]] = grid[coord[0]][coord[1]]

    for coord in coords:
        grid[coord[0]][coord[1]] = "."


def try_move(grid, coords, move):
    new_coords = [(coord[0] + move[0], coord[1] + move[1]) for coord in coords]

    # Something's in the way of the robot or at least one of the boxes
    if any(map(lambda coord: grid[coord[0]][coord[1]] == "#", new_coords)):
        return False

    # Nothing's in the way, so we can move
    if all(map(lambda coord: grid[coord[0]][coord[1]] == ".", new_coords)):
        move_forward(grid, coords, new_coords)
        return True

    # There's boxes in front of us, so let's see what's in front of them...
    else:
        new_coord_set = set(new_coords)
        for idx, coord in enumerate(new_coords):
            val = grid[coord[0]][coord[1]]
            # Boxes will be 2 characters wide if we're moving up or down
            if val in ["[", "]"] and move in [(1, 0), (-1, 0)]:
                new_coord_set.add(
                    (coord[0], coord[1] + 1 if val == "[" else coord[1] - 1)
                )

            # Careful, we don't want to recurse if there isn't anything on one side of the box!
            elif val == ".":
                new_coord_set.remove(coord)

        can_move = try_move(grid, list(new_coord_set), move)
        if can_move:
            move_forward(grid, coords, new_coords)

        return can_move


def move_boxes(input):
    grid, moves = parse_input(input)

    robot_coord = get_robot_coord(grid)

    for move in moves:
        if try_move(grid, [robot_coord], move):
            new_coord = (robot_coord[0] + move[0], robot_coord[1] + move[1])
            grid[robot_coord[0]][robot_coord[1]] = "."
            grid[new_coord[0]][new_coord[1]] = "@"
            robot_coord = new_coord

    sum = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if grid[y][x] == "[":
                sum += (100 * y) + x

    return sum


def driver():
    SAMPLE_EXPECTED = 9021
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
