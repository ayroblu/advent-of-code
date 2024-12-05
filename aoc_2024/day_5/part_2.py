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
    was_invalid = False
    pos = dict((v, i) for i, v in enumerate(update))
    for i in range(len(update)):
        num = update[i]
        required = prec[num].intersection(nums)
        while not seen.issuperset(required):
            # main logic here
            was_invalid = True
            for c, item in enumerate(required.difference(seen)):
                idx = pos[item]
                update.insert(i, update.pop(idx))
            pos = dict((v, i) for i, v in enumerate(update))
            num = update[i]
            required = prec[num].intersection(nums)
        seen.add(num)
    else:
        assert(len(update) % 2 == 1)
        if was_invalid:
            total += int(update[(len(update) - 1) // 2])

print(total)
