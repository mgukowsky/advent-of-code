#!/usr/bin/env python3

# https://adventofcode.com/2023/day/1

from functools import reduce
from num2words import num2words
from word2number import w2n
import re

DIGIT_STRINGS = "|".join([num2words(num) for num in range(1,10)])

# We need the lookahead assertion since otherwise re.findall won't detect overlapping matches
#   w/o lookahead (WRONG): 'twone' => ['two']
#   w/ lookahead (CORRECT): 'twone' => ['two', 'one']
# per https://stackoverflow.com/a/11430936
DIGIT_REGEX=f"(?=([1-9]|{DIGIT_STRINGS}))"

def get_line_digits(sum, line):
    matches = re.findall(DIGIT_REGEX, line)
    return sum + int("".join([str(w2n.word_to_num(match)) for match in [matches[0], matches[-1]]]))

with open('input.txt') as file:
    print(reduce(get_line_digits, file, 0));

