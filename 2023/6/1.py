#!/usr/bin/env python3

# https://adventofcode.com/2023/day/6

from functools import cache, reduce
import re

def eval_race(sum, race):

    time = race[0]
    distance = race[1]

    ways = 0
    for i in range(1, time+1):
        if (time - (i)) * i > distance:
            ways = ways + 1

    return sum * ways if sum > 0 else ways

with open('input.txt') as file:
    lines = file.readlines()

    times = [int(i) for i in re.findall(r"\d+", lines[0])]
    distances = [int(i) for i in re.findall(r"\d+", lines[1])]

    print(reduce(eval_race, zip(times, distances), 0))


