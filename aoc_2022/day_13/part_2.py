import json
from functools import cmp_to_key
from typing import Union

from utils.file import read_input

contents = read_input(__file__)
contents += """
[[2]]
[[6]]"""

lines = [json.loads(line) for line in contents.split("\n") if line]

type Input = list[Union[int, Input]]


def check(line1: Input, line2: Input) -> int:
    for i in range(len(line1)):
        if i >= len(line2):
            return 1
        a = line1[i]
        b = line2[i]
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return -1
            elif a > b:
                return 1
        elif isinstance(a, list) and isinstance(b, list):
            result = check(a, b)
            if result != 0:
                return result
        elif isinstance(a, int) and isinstance(b, list):
            result = check([a], b)
            if result != 0:
                return result
        elif isinstance(a, list) and isinstance(b, int):
            result = check(a, [b])
            if result != 0:
                return result
    if len(line2) > len(line1):
        return -1
    return 0


lines.sort(key=cmp_to_key(check))
i1 = lines.index([[2]]) + 1
i2 = lines.index([[6]]) + 1
print(i1, i2)
print(i1 * i2)
