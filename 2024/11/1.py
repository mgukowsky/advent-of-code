#!/usr/bin/env python3


import sys

SAMPLE_INPUT = """\
125 17
"""


def parse_input(input):
    return [int(n) for n in input.split(" ")]


def blink_stones(input):
    stones = parse_input(input)

    for i in range(25):
        new_stones = []
        for idx, stone in enumerate(stones):
            if stone == 0:
                new_stones.append(1)
            else:
                stonestr = str(stone)
                if len(stonestr) % 2 == 0:
                    midpoint = int(len(stonestr) / 2)
                    new_stones.append(int(stonestr[:midpoint]))
                    new_stones.append(int(stonestr[midpoint:]))
                else:
                    new_stones.append(stone * 2024)

        stones = new_stones

    return len(stones)


def driver():
    SAMPLE_EXPECTED = 55312
    SAMPLE_ACTUAL = blink_stones(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(blink_stones(f.read()))


if __name__ == "__main__":
    driver()
