#!/usr/bin/env python3

import re
import sys
from collections import namedtuple
from functools import cache

SAMPLE_INPUT = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

ClawSpec = namedtuple("ClawSpec", ["a", "b", "prize"])


def parse_input(input):
    raw = [line for line in input.splitlines()]
    raw.append("")

    output = []
    while len(raw) > 0:
        ax, ay = re.findall(r"[0-9]+", raw.pop(0))
        bx, by = re.findall(r"[0-9]+", raw.pop(0))
        px, py = re.findall(r"[0-9]+", raw.pop(0))
        output.append(
            ClawSpec(
                a=(int(ax), int(ay)), b=(int(bx), int(by)), prize=(int(px), int(py))
            )
        )
        raw.pop(0)

    return output


@cache
def evaluate_claw_spec(claw_spec, a_tokens, b_tokens):
    if a_tokens > 100 or b_tokens > 100:
        return -1

    a_sum = (claw_spec.a[0] * a_tokens, claw_spec.a[1] * a_tokens)
    b_sum = (claw_spec.b[0] * b_tokens, claw_spec.b[1] * b_tokens)

    sum = (a_sum[0] + b_sum[0], a_sum[1] + b_sum[1])

    if sum[0] > claw_spec.prize[0] or sum[1] > claw_spec.prize[1]:
        return -1
    elif sum[0] == claw_spec.prize[0] and sum[1] == claw_spec.prize[1]:
        return (a_tokens * 3) + b_tokens

    a_inc = evaluate_claw_spec(claw_spec, a_tokens + 1, b_tokens)
    b_inc = evaluate_claw_spec(claw_spec, a_tokens, b_tokens + 1)

    if a_inc > -1 and b_inc > -1:
        return min(a_inc, b_inc)
    elif a_inc > -1:
        return a_inc
    elif b_inc > -1:
        return b_inc
    else:
        return -1


def min_tokens(input):
    claw_specs = parse_input(input)

    total_tokens = 0
    for claw_spec in claw_specs:
        num_tokens = evaluate_claw_spec(claw_spec, 0, 0)
        if num_tokens > -1:
            total_tokens += num_tokens

    return total_tokens


def driver():
    SAMPLE_EXPECTED = 480
    SAMPLE_ACTUAL = min_tokens(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(min_tokens(f.read()))


if __name__ == "__main__":
    driver()
