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
    spring = "?".join([spring for _ in range(5)])
    meta = match.group(2)
    meta = ",".join([meta for _ in range(5)])
    meta_int = [int(i) for i in meta.split(",")]

    def get_counts(s: str, index: int) -> tuple[str, int]:
        count = 0
        agg: list[int] = []
        for i, char in enumerate(s):
            if i > index:
                res = [str(a) for a in agg]
                return ("".join(res), count)
            if char == '#':
                count += 1
            elif char == '.' and count > 0:
                agg.append(count)
                count = 0
            elif char == '?':
                res = [str(a) for a in agg]
                return ("".join(res), count)
        if count > 0 and index == len(s) - 1:
            agg.append(count)
            count = 0
        res = [str(a) for a in agg]
        return ("".join(res), 0)

    possible_spring: dict[str, dict[int, int]] = {"": {0: 1}}

    for i, char in enumerate(spring):
        new_possible_spring: dict[str, dict[int, int]] = {}
        for prev_key, value in possible_spring.items():
            for last, count in value.items():
                possibilities = [".", "#"]
                if char != '?':
                    possibilities = [char]
                for s in possibilities:
                    new_spr = "#"*last + s + spring[i + 1:]
                    index = i - (len(spring) - len(new_spr))
                    part_key, new_last = get_counts(new_spr, index)
                    key = prev_key
                    if prev_key and part_key:
                        key = prev_key + "," + part_key
                    elif part_key:
                        key = part_key
                    if new_last:
                        idx = 0
                        if key:
                            idx = len(key.split(","))
                        if idx >= len(meta_int):
                            continue
                        if meta_int[idx] < new_last:
                            continue
                    if len(key) > len(meta):
                        continue
                    if meta.startswith(key):
                        if key not in new_possible_spring:
                            new_possible_spring[key] = {}
                        temp = count
                        if new_last in new_possible_spring[key]:
                            temp += new_possible_spring[key][new_last]
                        new_possible_spring[key][new_last] = temp
        possible_spring = new_possible_spring
    running_sum = possible_spring[meta][0]
    sum += running_sum


print(sum)
