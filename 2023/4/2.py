#!/usr/bin/env python3

# https://adventofcode.com/2023/day/4

from functools import reduce
import re
import operator

with open('input.txt') as file:
    lines = file.readlines()
    cache = {}
    for i in range(len(lines)):
        cache[i] = cache.get(i, 0) + 1
        line = lines[i]
        nums = [set(re.findall(r"\d+", numstr)) for numstr in line[line.index(":"):].split("|")]
        winning_nums = nums[0] & nums[1]

        for j in range(len(winning_nums)):
            cache[i + j + 1] = cache.get(i + j + 1, 0) + cache[i]

    print(sum(cache.values()))

