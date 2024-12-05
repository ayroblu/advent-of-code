from typing import DefaultDict
from utils.file import read_input
from collections import defaultdict

contents = read_input(__file__)
rules, updates = contents.strip().split("\n\n")
rules = rules.splitlines()
updates = [update.split(",") for update in updates.splitlines()]

prec: DefaultDict[str,set[str]] = defaultdict(set)
for rule in rules:
    before, after = rule.split("|")
    prec[after].add(before)

total = 0
for update in updates:
    seen = set[str]()
    nums = set(update)
    for num in update:
        required = prec[num]
        if not seen.issuperset(required.intersection(nums)):
            break
        seen.add(num)
    else:
        assert(len(update) % 2 == 1)
        total += int(update[(len(update) - 1) // 2])

print(total)
