#!/usr/bin/env python3

import hashlib
import re
import sys

EXAMPLES = []


def parse_input(input):
    output = []

    for line in input.splitlines():
        output.extend([c for c in line])

    return output


def get_md5(key, n):
    hash_str = f"{key}{n}"
    h = hashlib.md5()
    h.update(bytes(hash_str, "utf-8"))
    return h.hexdigest()


def solution(input):
    key = "".join(parse_input(input))

    n = 0
    while True:
        if re.match(r"^0{6}", get_md5(key, n)):
            return n
        n += 1


if __name__ == "__main__":
    for example, expected in EXAMPLES:
        actual = solution(example)
        if actual != expected:
            print(f"❗Example case failed; expected: {expected}, actual: {actual}")
            sys.exit(1)

    print("✅ Example cases passed")

    with open("input.txt", "r") as f:
        print(solution(f.read()))
