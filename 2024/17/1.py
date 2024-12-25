#!/usr/bin/env python3

import re
import sys
from dataclasses import dataclass

SAMPLE_INPUT = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""


def parse_input(input):
    lines = [*input.splitlines()]
    A = int(re.findall(r"[0-9]+", lines.pop(0))[0])
    B = int(re.findall(r"[0-9]+", lines.pop(0))[0])
    C = int(re.findall(r"[0-9]+", lines.pop(0))[0])
    lines.pop(0)
    prog = [int(n) for n in re.findall(r"[0-9]+", lines.pop())]

    return A, B, C, prog


@dataclass
class CPU:
    A: int
    B: int
    C: int
    PC: int
    prog: list[int]
    output: list[int]

    def __init__(self, A: int, B: int, C: int, prog: list[int]):
        self.A = A
        self.B = B
        self.C = C
        self.PC = 0
        self.output = []
        self.prog = prog

    def run(self):
        while self.PC < len(self.prog):
            self._exec(self._fetch(), self._fetch())

    def _exec(self, opcode, operand):
        match opcode:
            case 0:
                self._adv(operand)
            case 1:
                self._bxl(operand)
            case 2:
                self._bst(operand)
            case 3:
                self._jnz(operand)
            case 4:
                self._bxc(operand)
            case 5:
                self._out(operand)
            case 6:
                self._bdv(operand)
            case 7:
                self._cdv(operand)

    def _fetch(self):
        out = self.prog[self.PC]
        self.PC += 1
        return out

    def _get_combo_operand(self, operand):
        if operand < 4:
            return operand
        elif operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        else:  # operand == 6:
            return self.C

    def _adv(self, operand):
        self.A = int(self.A / (2 ** self._get_combo_operand(operand)))

    def _bxl(self, operand):
        self.B ^= operand

    def _bst(self, operand):
        self.B = self._get_combo_operand(operand) % 8

    def _jnz(self, operand):
        if self.A != 0:
            self.PC = operand

    def _bxc(self, operand):
        self.B ^= self.C

    def _out(self, operand):
        self.output.append(self._get_combo_operand(operand) % 8)

    def _bdv(self, operand):
        self.B = int(self.A / (2 ** self._get_combo_operand(operand)))

    def _cdv(self, operand):
        self.C = int(self.A / (2 ** self._get_combo_operand(operand)))


def run_prog(input):
    cpu = CPU(*parse_input(input))
    cpu.run()
    return ",".join([str(n) for n in cpu.output])


def driver():
    SAMPLE_EXPECTED = "4,6,3,5,6,3,5,2,1,0"
    SAMPLE_ACTUAL = run_prog(SAMPLE_INPUT)
    if SAMPLE_EXPECTED == SAMPLE_ACTUAL:
        print("✅ Sample input passed")
    else:
        print(
            f"❗Sample input incorrect; expected: {SAMPLE_EXPECTED}, actual: {SAMPLE_ACTUAL}"
        )

        sys.exit(1)

    with open("input.txt", "r") as f:
        print(run_prog(f.read()))


if __name__ == "__main__":
    driver()
