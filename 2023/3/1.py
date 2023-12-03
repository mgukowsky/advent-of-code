#!/usr/bin/env python3

# https://adventofcode.com/2023/day/3

import re

def extract_syms(line):
    return set([match.start() for match in re.finditer(r"[^\.^\d]", line)])

def eval_line(lines, idx):
    prev_syms = extract_syms(lines[idx-1])
    line_syms = extract_syms(lines[idx])
    next_syms = extract_syms(lines[idx+1])
    line_nums = [match.span() for match in re.finditer(r"\d+", lines[idx])]

    sum = 0

    # Check if each digit in each candidate number is adjacent to a symbol
    for num in line_nums:
        for digit_idx in range(num[0]-1, num[1]+1): # offsets account for diagonals
            if digit_idx in prev_syms or digit_idx in line_syms or digit_idx in next_syms:
                sum = sum + int(lines[idx][num[0]:num[1]])
                break

    return sum


with open('input.txt') as file:
    lines = [line.strip() for line in file]

    # Pad with empty lines to help out sliding window approach
    lines.insert(0, "")
    lines.append("")

    WINDOW_SIZE = 3

    sum = 0
    # Use a sliding window to compare a single line against the previous 
    # and next one. Snippet from https://stackoverflow.com/a/6822773
    for i in range(len(lines) - WINDOW_SIZE + 1):
        sum = sum + eval_line(lines, i+1)

    print(sum)
