import re
from utils.file import read_file
from utils.types import not_none


contents = read_file(__file__, "input")
lines = contents.split("\n")
sum = 0
pat = r"^([\.?#]+) ([\d,]+)$"
regex = re.compile(pat)
for line in lines:
    match = not_none(regex.match(line))
    spring = match.group(1)
    meta = [int(i) for i in match.group(2).split(",")]
    possible_spring = [spring]
    for i, char in enumerate(spring):
        if char != '?':
            continue
        new_possible_spring: list[str] = []
        for spr in possible_spring:
            for s in [".", "#"]:
                new_possible_spring.append(spr[:i] + s + spr[i + 1:])
        possible_spring = new_possible_spring
    running_sum = 0
    for s in possible_spring:
        count = 0
        agg: list[int] = []
        for char in s:
            if char == '#':
                count += 1
            elif char == '.' and count > 0:
                agg.append(count)
                count = 0
        if count > 0:
            agg.append(count)
            count = 0
        if agg == meta:
            running_sum += 1
    sum += running_sum


print(sum)
