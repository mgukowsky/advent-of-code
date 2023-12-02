#!/usr/bin/env python3

# https://adventofcode.com/2023/day/1

from functools import reduce

def get_line_digits(sum, line):
    digits = [char for char in line if char.isdigit()]
    return sum + int("".join([digits[0], digits[-1]]))

with open('input.txt') as file:
    print(reduce(get_line_digits, file, 0));

