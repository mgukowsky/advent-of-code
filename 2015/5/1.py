#!/usr/bin/env python3

import re
import sys
from itertools import pairwise, starmap

EXAMPLES = [
    ("ugknbfddgicrmopn", 1),
    ("aaa", 1),
    ("jchzalrnumimnmhp", 0),
    ("haegwjzuvuyypxyu", 0),
    ("dvszwmarrgswjxmb", 0),
]


def parse_input(input):
    return [line for line in input.splitlines()]


def has_double_letter(str_to_test):
    return any(starmap(lambda lhs, rhs: lhs == rhs, pairwise(str_to_test)))


def is_nice(str_to_test):
    return (
        len(re.findall(r"[a|e|i|o|u]", str_to_test)) >= 3
        and has_double_letter(str_to_test)
        and len(re.findall(r"ab|cd|pq|xy", str_to_test)) == 0
    )


def solution(input):
    return sum(map(lambda str_to_test: is_nice(str_to_test), parse_input(input)))


if __name__ == "__main__":
    for example, expected in EXAMPLES:
        actual = solution(example)
        if actual != expected:
            print(f"❗Example case failed; expected: {expected}, actual: {actual}")
            sys.exit(1)

    print("✅ Example cases passed")

    with open("input.txt", "r") as f:
        print(solution(f.read()))
