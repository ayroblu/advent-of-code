import re

from utils.file import read_input
from utils.types import not_none

contents = read_input(__file__)
# contents = """px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}"""

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

pat = re.compile(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
parts: list[tuple[int, int, int, int]] = []
for line in res.splitlines():
    x, m, a, s = not_none(pat.match(line)).groups()
    parts.append((int(x), int(m), int(a), int(s)))

total = 0
for part in parts:
    x, m, a, s = part
    wf = "in"
    while True:
        conds, last = workflows[wf]
        next = None
        for name, op, val, result in conds:
            part_val = part["xmas".index(name)]
            if op == ">":
                if part_val > val:
                    next = result
                    break
            if op == "<":
                if part_val < val:
                    next = result
                    break
        if next is None:
            next = last
        if next == "A":
            total += x + m + a + s
            break
        if next == "R":
            break
        wf = next

print(total)
