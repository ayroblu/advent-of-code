import re
from typing import Iterable

from utils.file import read_input
from utils.types import not_none

contents = read_input(__file__)

wf, res = contents.split("\n\n")
pat = re.compile(r"([amsx])([<>])(\d+):(\w+)")
workflows: dict[str, tuple[list[tuple[str, str, int, str]], str]] = {}
for line in wf.splitlines():
    name, cond_str = line.split("{")
    conds = cond_str[:-1].split(",")
    last = conds.pop()
    workflow_conds: list[tuple[str, str, int, str]] = []
    for cond in conds:
        part, op, num_str, next = not_none(pat.match(cond)).groups()
        workflow_conds.append((part, op, int(num_str), next))
    workflows[name] = (workflow_conds, last)

type Cond = tuple[str, str, int]
result_branches: list[list[Cond]] = []


def get_paths(key: str, history: list[Cond] = []) -> None:
    conds, last = workflows[key]
    for cond in conds:
        part, op, val, result = cond

        if result == "A":
            result_branches.append(history + [(part, op, val)])
        elif result != "R":
            get_paths(result, history + [(part, op, val)])

        if op == ">":
            rev_cond = (part, "<", val + 1)
        else:
            rev_cond = (part, ">", val - 1)
        history += [rev_cond]
    if last == "R":
        pass
    elif last == "A":
        result_branches.append(history)
    else:
        get_paths(last, history)


get_paths("in")


def mult(iterable: Iterable[int]) -> int:
    total = 1
    for i in iterable:
        total *= i
    return total


total = 0
for history in result_branches:
    # switch from exclusive to [inclusive, exclusive) bounds
    conditions: dict[str, tuple[int, int]] = {key: (1, 4001) for key in "xmas"}
    for part, op, val in history:
        low, high = conditions[part]
        if op == ">":
            # [1, 2001], > 2000
            if val >= high - 1:
                break
            conditions[part] = (max(low, val + 1), high)
        if op == "<":
            if val <= low:
                break
            conditions[part] = (low, min(high, val))
    else:
        total += mult(high - low for _, (low, high) in conditions.items())

print(total)
