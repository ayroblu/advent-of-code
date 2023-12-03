import re

from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.split("\n")

sum = 0
digit_regex = re.compile(r"\d+")
gear_regex = re.compile(r"[*]")
for index, line in enumerate(lines):
    if not line:
        continue
    matches = gear_regex.finditer(line)
    for match in matches:
        start_index, end_index = match.span()
        nums: list[int] = []
        for i, l in enumerate(lines[max(index - 1, 0) : min(index + 2, len(lines))]):
            for match in digit_regex.finditer(l):
                match_start, match_end = match.span()
                if index == i and match_start == end_index or match_end == start_index:
                    nums.append(int(match.group()))
                elif match_start <= start_index + 1 and match_end >= end_index - 1:
                    nums.append(int(match.group()))
        if len(nums) == 2:
            sum += nums[0] * nums[1]


print(sum)
