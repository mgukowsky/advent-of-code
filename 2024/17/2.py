#!/usr/bin/env python3

import re
import sys
from dataclasses import dataclass

SAMPLE_INPUT = """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
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

    def dump(self):
        print(
            f"A: {self.A}, B: {self.B}, C: {self.C}, PC: {self.PC}, output: {self.output}"
        )

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


def get_period(A, B, C, prog):
    period = 0

    initial_cpu = CPU(A, B, C, prog)
    initial_cpu.run()

    initial_output = initial_cpu.output

    while True:
        period += 1
        cpu = CPU(A + period, B, C, prog)
        cpu.run()
        if cpu.output[1] != initial_output[1]:
            break

    return period


def run_prog(input):
    A, B, C, prog = parse_input(input)
    prog_str = ",".join([str(n) for n in prog])
    A = 8 ** (len(prog) - 1)

    period = get_period(A, B, C, prog)

    while True:
        print(f"A is {A}")
        cpu = CPU(A, B, C, prog)
        cpu.run()
        prog_output = ",".join([str(n) for n in cpu.output])
        if prog_output == prog_str:
            return A
        else:
            cpu.dump()
            A += 1


def driver():
    SAMPLE_EXPECTED = 117440
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
