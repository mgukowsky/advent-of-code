#!/usr/bin/env python3

import sys

SAMPLE_INPUT = """\
2333133121414131402
"""


def parse_input(input):
    output = [int(c) for c in input.strip()]

    # Append space qualifier to the last file if it's missing
    if len(output) % 2 != 0:
        output.append(0)

    return output


def get_checksum(input):
    file_list = parse_input(input)

    tail_ptr = len(file_list)
    tail_file_idx = int(len(file_list) / 2)
    tail_file_blocks = 0
    head_ptr = 0

    file_idx = 0
    block_idx = 0
    tail_block_idx = sum(file_list)
    total = 0

    while block_idx < tail_block_idx:
        el = file_list[head_ptr]
        if head_ptr % 2 == 0:
            for i in range(el):
                print(file_idx)
                total += file_idx * block_idx
                block_idx += 1
                print(f"A bi:{block_idx} ti:{tail_block_idx}")
                if block_idx >= tail_block_idx:
                    break
            file_idx += 1

        else:
            for i in range(el):
                if tail_file_blocks == 0:
                    tail_file_idx -= 1
                    tail_ptr -= 2
                    tail_file_blocks = file_list[tail_ptr]
                    tail_block_idx -= file_list[tail_ptr + 1]

                print(tail_file_idx)
                total += tail_file_idx * block_idx
                block_idx += 1
                tail_block_idx -= 1
                tail_file_blocks -= 1
                print(f"B bi:{block_idx} ti:{tail_block_idx}")
                if block_idx >= tail_block_idx:
                    break

        print("END")
        head_ptr += 1

    return total


def driver():
    SAMPLE_EXPECTED = 1928
    SAMPLE_ACTUAL = get_checksum(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(get_checksum(f.read()))


if __name__ == "__main__":
    driver()
