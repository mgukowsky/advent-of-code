#!/usr/bin/env python3

import re
import sys

SAMPLE_INPUT = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


# Map each number to the numbers that must appear after it
def build_rules_map(rules):
    rules_map = {}

    for rule in rules:
        before, after = rule

        if before not in rules_map:
            rules_map[before] = set([after])
        else:
            rules_map[before].add(after)

    return rules_map


def parse_input(input):
    # Track our mode: either parsing a rule or parsing an update
    parsing_rules = True
    rules_list = []
    update_list = []

    for line in input.splitlines():
        if len(line) == 0:
            parsing_rules = False
        elif parsing_rules:
            before, after = map(int, re.findall(r"[0-9]+", line))
            rules_list.append((before, after))
        else:
            update_list.append([int(x) for x in line.split(",")])

    return (rules_list, update_list)


# If we have already seen a number that is in the rule for the current number, then the update is in violation of the rule
def does_follow_rule(seen, rule):
    return not any([el in rule for el in seen])


def sum_correct_rules(input):
    rules, updates = parse_input(input)

    rules_map = build_rules_map(rules)

    sum = 0

    for update in updates:
        seen = set()
        valid = True

        for el in update:
            if el in rules_map and not does_follow_rule(seen, rules_map[el]):
                valid = False
                break
            else:
                seen.add(el)

        if valid:
            sum += update[int(len(update) / 2)]

    return sum


def driver():
    SAMPLE_EXPECTED = 143
    SAMPLE_ACTUAL = sum_correct_rules(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(sum_correct_rules(f.read()))


if __name__ == "__main__":
    driver()
