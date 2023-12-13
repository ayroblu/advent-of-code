import re
from itertools import batched

from utils.file import read_input
from utils.types import not_none

contents = read_input(__file__)

problem, moves = contents.split("\n\n")
lines = problem.splitlines()
lines.pop()
stacks = [map(lambda x: x[1], batched(line, 4)) for line in lines]
stacks = [list(reversed(list(filter(lambda x: x != " ", i)))) for i in zip(*stacks)]
pat = re.compile(r"move (\d+) from (\d+) to (\d+)")
for line in moves.splitlines():
    match = not_none(pat.match(line))
    num, from_num, to = map(int, match.groups())
    for _ in range(num):
        stacks[to - 1].append(stacks[from_num - 1].pop())

top = "".join([stack.pop() for stack in stacks])
print(top)
