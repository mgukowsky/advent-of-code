#!/usr/bin/env python3

import sys

EXAMPLES = [
    ("^v", 3),
    ("^>v<", 3),
    ("^v^v^v^v^v", 11),
]


def parse_input(input):
    output = []

    for line in input.splitlines():
        output.extend([c for c in line])

    return output


def get_move(dir):
    match dir:
        case "^":
            return (-1, 0)
        case ">":
            return (0, 1)
        case "v":
            return (1, 0)
        case "<":
            return (0, -1)


def solution(input):
    dirs = parse_input(input)

    santa_pos = (0, 0)
    robo_santa_pos = santa_pos
    visited = set([santa_pos])

    santa_should_move = True
    for dir in dirs:
        move = get_move(dir)
        if santa_should_move:
            santa_pos = (santa_pos[0] + move[0], santa_pos[1] + move[1])
            visited.add(santa_pos)
        else:
            robo_santa_pos = (robo_santa_pos[0] + move[0], robo_santa_pos[1] + move[1])
            visited.add(robo_santa_pos)

        santa_should_move = not santa_should_move

    return len(visited)


if __name__ == "__main__":
    for example, expected in EXAMPLES:
        actual = solution(example)
        if actual != expected:
            print(f"❗Example case failed; expected: {expected}, actual: {actual}")
            sys.exit(1)

    print("✅ Example cases passed")

    with open("input.txt", "r") as f:
        print(solution(f.read()))
