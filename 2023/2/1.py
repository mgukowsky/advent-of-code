#!/usr/bin/env python3

# https://adventofcode.com/2023/day/2

from functools import reduce
import re

BAG_CONTENTS = { "red": 12, "green": 13, "blue": 14 }

def add_game_id_if_valid(sum, line):
    # 1 is the index of the first subgroup; see 
    # https://docs.python.org/3/library/re.html#re.Match.group
    game_id = int(re.match(r"Game (\d+):", line).group(1))
    set_infos = line[line.index(":"):].strip()
    parsed_sets = [dict((k, int(v)) for v, k in re.findall(r"(\d+) (\w+)", info)) for info in set_infos.split(";")]
    for set_info in parsed_sets:
        for color, quantity in set_info.items():
            if BAG_CONTENTS[color] < quantity:
                return sum
    return sum + game_id

with open('input.txt') as file:
    print(reduce(add_game_id_if_valid, file, 0));

