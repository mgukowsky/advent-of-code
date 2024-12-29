#!/usr/bin/env python3

import re
import sys
from collections import deque
from itertools import islice, pairwise

EXAMPLES = [
    ("qjhvhtzxzqqjkmpb", 1),
    ("xxyxx", 1),
    ("uurcxstgmygtbstg", 0),
    ("ieodomkazucvgmuy", 0),
]


def parse_input(input):
    return [line for line in input.splitlines()]


def has_double_letter_rep(str_to_test):
    doublets = set()
    # Prevent false positives on strings like "aaa"
    prev_doublet = None
    for doublet in pairwise(str_to_test):
        if doublet in doublets and doublet != prev_doublet:
            return True
        else:
            doublets.add(doublet)
            prev_doublet = doublet

    return False


def has_aba_string(input):
    # Based on sliding window recipe in https://docs.python.org/3/library/itertools.html
    iterator = iter(input)
    window = deque(islice(iterator, 2), maxlen=3)
    for el in iterator:
        window.append(el)
        if len(window) > 2 and window[0] == window[2]:
            return True

    return False


def is_nice(str_to_test):
    return has_double_letter_rep(str_to_test) and has_aba_string(str_to_test)


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
