#!/usr/bin/env python3

# https://adventofcode.com/2023/day/4

from functools import reduce
import re
import operator

def add_winning_numbers(sum, line):
    nums = [set(re.findall(r"\d+", numstr)) for numstr in line[line.index(":"):].split("|")]
    winning_nums = nums[0] & nums[1]
    if len(winning_nums) > 0:
        return sum + (2 ** (len(winning_nums) - 1))
    else:
        return sum

with open('input.txt') as file:
    print(reduce(add_winning_numbers, file, 0));

