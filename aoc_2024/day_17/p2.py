import re
from itertools import batched

from utils.file import read_input

contents = read_input(__file__).strip()

registers_text, program = contents.split("\n\n")
a, b, c = list(map(int, re.findall(r"\d+", registers_text)))
instructions = list(map(int, re.findall(r"\d+", program)))
inst = list(batched(instructions, 2))


def run(a: int, b: int, c: int) -> list[int]:
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
        # print(instruction, op, "--", a, b, c)

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
    return out


def recur(result: list[int] = []):
    current = "".join([format(x, "03b") for x in result])
    for v in range(8):
        a = int(current + format(v, "03b"), 2)
        out = run(a, b, c)
        if out == instructions[-1 - len(result) :]:
            if len(out) < len(instructions):
                recur(result + [v])
            else:
                print(a)


recur()

input = """Register A: 35200350
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,7,1,3,5,5,0,3,3,0"""
# 3,0 - exit if 0 else go to start
# 0,3 - exit if a < 8 else a //= 2**3
# 5,5 - out b % 8
# 1,3 - b^=3
# 4,7 - b^=c
# 7,5 - c= a // 2**b (truncate a from right by b count)
# 1,2 - b^=2
# 2,4 - b=a % 8
# b is 0 - 7
# b is [2, 3, 0, 1, 6, 7, 4, 5]
# b is (a truncate b)^b^3
