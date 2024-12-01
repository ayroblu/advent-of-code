import re
from typing import DefaultDict
from utils.file import read_file
from collections import defaultdict


contents = read_file(__file__, "input")
lines = contents.strip().split("\n")
all = [(int(x) for x in re.split(r' +', line)) for line in lines]
left, right = [list(x) for x in zip(*all)]

store: DefaultDict[int, list[int]] = defaultdict(list)
for item in right:
    store[item].append(item)

sum = 0
for item in left:
    sum += item * len(store[item])


print(sum)


