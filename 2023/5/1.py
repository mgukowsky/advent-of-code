#!/usr/bin/env python3

# https://adventofcode.com/2023/day/4

from functools import reduce
import re
import operator
from dataclasses import dataclass

@dataclass
class Mapping:
    start: int
    extent: int
    delta: int

def build_transform(map_details):
    mappings = []

    for details in map_details:
        details = [int(i) for i in details]
        mappings.append(Mapping(details[1], details[2], details[0] - details[1]))

    return mappings

def apply_transforms(transforms, seeds):
    for transform in transforms:
        for i in range(len(seeds)):
            seed = seeds[i]
            # Find the mapping within the transform that is in the range of the seed
            valid_mapping = next((mapping for mapping in transform if seed >= mapping.start and seed < mapping.start + mapping.extent), None)

            if valid_mapping is not None:
                seeds[i] = seed + valid_mapping.delta

    return seeds

with open('input.txt') as file:
    lines = file.readlines()
    lines.append("") # pad with an empty line to ensure we parse all of the transforms

    seeds = re.findall(r"\d+", lines[0])
    seeds = [int(i) for i in seeds]

    transforms = []
    map_lines = []

    # Create a series of transforms which we will pass each seed through
    for line in lines[2:]:
        line = line.strip()
        if re.search(r"map:$", line):
            continue
        elif len(line) == 0:
            transforms.append(build_transform(map_lines))
            map_lines = []
        else:
            map_lines.append(re.findall(r"\d+", line))

         
    print(min(apply_transforms(transforms, seeds)))

