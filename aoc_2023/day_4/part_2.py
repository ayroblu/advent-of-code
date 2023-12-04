import re

from utils.file import read_file
from utils.types import not_none

contents = read_file(__file__, "input")
lines = contents.split("\n")
sum = 0
regex = re.compile(r"Card +(\d+): (.*) \| (.*)")
split_regex = re.compile(r" +")
copies: dict[str, int] = {}
for line in lines:
    if not line:
        continue
    match = not_none(regex.match(line))
    winnersStr = re.split(r" +", match.group(2).strip())
    winners = {int(i) for i in winnersStr}
    numsStr = re.split(r" +", match.group(3).strip())
    nums = [int(i) for i in numsStr if int(i) in winners]
    card_num = match.group(1)
    num_copies = copies[card_num] if card_num in copies else 1
    for i in range(1, len(nums) + 1):
        next_card_num = str(int(card_num) + i)
        current_copies = copies[next_card_num] if next_card_num in copies else 1
        copies[next_card_num] = num_copies + current_copies
    sum += num_copies


print(sum)
