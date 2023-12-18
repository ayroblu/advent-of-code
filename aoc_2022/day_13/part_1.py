import json
from typing import Union

from utils.file import read_input

contents = read_input(__file__)

pairs = contents.split("\n\n")

type Input = list[Union[int, Input]]


def check(line1: Input, line2: Input) -> Union[bool, None]:
    for i in range(len(line1)):
        if i >= len(line2):
            return False
        a = line1[i]
        b = line2[i]
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return True
            elif a > b:
                return False
        elif isinstance(a, list) and isinstance(b, list):
            result = check(a, b)
            if result is not None:
                return result
        elif isinstance(a, int) and isinstance(b, list):
            result = check([a], b)
            if result is not None:
                return result
        elif isinstance(a, list) and isinstance(b, int):
            result = check(a, [b])
            if result is not None:
                return result
    if len(line2) > len(line1):
        return True


sum = 0
for i, pair in enumerate(pairs):
    line1, line2 = [json.loads(line) for line in pair.splitlines()]
    result = check(line1, line2)
    if result:
        sum += i + 1
print(sum)
