import re
from itertools import batched

from utils.file import read_input

contents = read_input(__file__).strip()

registers_text, program = contents.split("\n\n")
a, b, c = list(map(int, re.findall(r"\d+", registers_text)))
instructions = list(map(int, re.findall(r"\d+", program)))
inst = list(batched(instructions, 2))


def combo(v: int) -> int:
    match v:
        case 0 | 1 | 2 | 3 as x:
            return x
        case 4 as x:
            return a
        case 5 as x:
            return b
        case 6 as x:
            return c
        case _:
            assert False


i = 0

out = list[int]()
while i >= 0 and i < len(inst):
    instruction, op = inst[i]

    match instruction:
        case 0:
            num = a
            den = 2 ** combo(op)
            a = num // den
        case 1:
            b ^= op
        case 2:
            b = combo(op) % 8
        case 3:
            if a == 0:
                pass
            else:
                i = op
                continue
        case 4:
            b ^= c
        case 5:
            out.append(combo(op) % 8)
        case 6:
            num = a
            den = 2 ** combo(op)
            b = num // den
        case 7:
            num = a
            den = 2 ** combo(op)
            c = num // den
        case _:
            assert False

    i += 1

print(",".join(map(str, out)))
