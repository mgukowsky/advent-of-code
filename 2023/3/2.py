#!/usr/bin/env python3

# https://adventofcode.com/2023/day/3

from functools import reduce
from operator import mul
import re

NOT_FOUND = -1

def extract_gears(line):
    return set([match.start() for match in re.finditer(r"\*", line)])

def eval_line(lines, idx, gearmap):
    prev_gears = extract_gears(lines[idx-1])
    line_gears = extract_gears(lines[idx])
    next_gears = extract_gears(lines[idx+1])
    line_nums = [match.span() for match in re.finditer(r"\d+", lines[idx])]

    # Check if each digit in each candidate number is adjacent to a symbol
    for num in line_nums:
        for digit_idx in range(num[0]-1, num[1]+1): # offsets account for diagonals
            matching_idx = NOT_FOUND
            if digit_idx in prev_gears:
                matching_idx = idx-1
            elif digit_idx in line_gears:
                matching_idx = idx
            elif digit_idx in next_gears:
                matching_idx = idx+1

            if matching_idx > NOT_FOUND:
                # Use the gear's XY coord as its unique identifier
                gearid = f"{matching_idx}_{digit_idx}"
                if gearid not in gearmap:
                    gearmap[gearid] = []

                gearmap[gearid].append(int(lines[idx][num[0]:num[1]]))

            # N.B. that unlike for part 1 we don't want to break, because a number can be touching
            # two different gears.

def calc_gear_ratio(sum, gear_nums):
    if len(gear_nums) == 2:
        return sum + reduce(mul, gear_nums)
    else:
        return sum

with open('input.txt') as file:
    lines = [line.strip() for line in file]

    # Pad with empty lines to enable our sliding window approach
    lines.insert(0, "")
    lines.append("")

    WINDOW_SIZE = 3

    gearmap = {}
    # Use a sliding window to compare a single line against the previous 
    # and next one. Snippet from https://stackoverflow.com/a/6822773
    for i in range(len(lines) - WINDOW_SIZE + 1):
        eval_line(lines, i+1, gearmap)

    print(reduce(calc_gear_ratio, gearmap.values(), 0))

