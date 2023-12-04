import re

from utils.file import read_file
from utils.types import not_none

contents = read_file(__file__, "input")
lines = contents.split("\n")
sum = 0
regex = re.compile(r"Card +\d+: (.*) \| (.*)")
split_regex = re.compile(r" +")
for line in lines:
    if not line:
        continue
    match = not_none(regex.match(line))
    winnersStr = re.split(r" +", match.group(1).strip())
    winners = {int(i) for i in winnersStr}
    numsStr = re.split(r" +", match.group(2).strip())
    nums = [int(i) for i in numsStr if int(i) in winners]
    if len(nums) > 0:
        result = 2 ** (len(nums) - 1)
        sum += result


print(sum)
