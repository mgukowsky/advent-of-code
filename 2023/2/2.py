#!/usr/bin/env python3

# https://adventofcode.com/2023/day/2

from functools import reduce
import operator
import re

def reduce_to_max(max, set_info):
    for color, quantity in set_info.items():
        if color not in max or max[color] < quantity:
            max[color] = quantity

    return max

def add_game_id_if_valid(sum, line):
    # 1 is the index of the first subgroup; see 
    # https://docs.python.org/3/library/re.html#re.Match.group
    game_id = int(re.match(r"Game (\d+):", line).group(1))
    set_infos = line[line.index(":"):].strip()
    parsed_sets = [dict((k, int(v)) for v, k in re.findall(r"(\d+) (\w+)", info)) for info in set_infos.split(";")]
    min_set = reduce(reduce_to_max, parsed_sets, {})
    return sum + reduce(operator.mul, min_set.values(), 1)

with open('input.txt') as file:
    print(reduce(add_game_id_if_valid, file, 0));

