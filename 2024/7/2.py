#!/usr/bin/env python3

import operator
import re
import sys

SAMPLE_INPUT = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def parse_input(input):
    output = []

    for line in input.splitlines():
        target, nums = line.split(":")
        output.append((int(target), [int(num) for num in re.findall(r"[0-9]+", nums)]))

    return output


def concat_op(lhs, rhs):
    return int(str(lhs) + str(rhs))


def do_is_valid_calibration(target, total, nums, op):
    # print(f"{target}; {total}; {nums}; {op};")
    if len(nums) == 0:
        if target == total:
            return True
        else:
            return False
    # Need to consider the corner case where there are still 1's left in the array
    elif total >= target and not all([n == 1 for n in nums]):
        return False
    else:
        next_num = nums.pop(0)
        new_total = op(total, next_num)
        return (
            do_is_valid_calibration(target, new_total, list(nums), operator.add)
            or do_is_valid_calibration(
                target,
                new_total,
                list(nums),
                operator.mul,
            )
            or do_is_valid_calibration(
                target,
                new_total,
                list(nums),
                concat_op,
            )
        )


def is_valid_calibration(target, nums):
    return (
        do_is_valid_calibration(target, nums[0], nums[1:], operator.add)
        or do_is_valid_calibration(
            target,
            nums[0],
            nums[1:],
            operator.mul,
        )
        or do_is_valid_calibration(
            target,
            nums[0],
            nums[1:],
            concat_op,
        )
    )


def sum_valid_calibrations(input):
    sum = 0

    for target, nums in parse_input(input):
        if is_valid_calibration(target, nums):
            sum += target

    return sum


def driver():
    SAMPLE_EXPECTED = 11387
    SAMPLE_ACTUAL = sum_valid_calibrations(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(sum_valid_calibrations(f.read()))


if __name__ == "__main__":
    driver()
