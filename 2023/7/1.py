#!/usr/bin/env python3

# https://adventofcode.com/2023/day/7

import heapq
import re

card_weights = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_map = {}
for i in reversed(range(len(card_weights))):
    card_map[card_weights[i]] = i

def parse_bid(line):
    hand, bid = line.split(" ")
    
    hand = set(re.findall(r"[A-Z0-9]", hand))
    bid = int(bid)

with open('input.txt') as file:
    bids = []

    for line in file:
        heapq.heappush()

