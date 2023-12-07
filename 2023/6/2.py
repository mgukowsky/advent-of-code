#!/usr/bin/env python3

# https://adventofcode.com/2023/day/6

from functools import cache, reduce
import re

def eval_race(time, distance):
    for i in range(1, time+1):
        if (time - (i)) * i > distance:
            min = i
            break

    for i in reversed(range(1, time+1)):
        if (time - (i)) * i > distance:
            max = i
            break

    return max - min + 1

with open('input.txt') as file:
    lines = file.readlines()

    time = int(re.sub(r"\s+", "", lines[0][lines[0].index(":")+1:]))
    distance = int(re.sub(r"\s+", "", lines[1][lines[1].index(":")+1:]))

    print(eval_race(time, distance))


