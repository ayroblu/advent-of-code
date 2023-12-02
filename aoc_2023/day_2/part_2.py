import re
from functools import reduce

from utils.file import read_file
from utils.types import not_none

contents = read_file(__file__, "input")
lines = contents.split("\n")

game_regex = re.compile(r"Game (\d+): (.*)$")
round_regex = re.compile(r"(\d+) (red|green|blue)")
sum = 0
for line in lines:
    if not line:
        continue
    match = not_none(game_regex.match(line))
    id = int(match.group(1))
    text = match.group(2)
    rounds = text.split(";")
    mins = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for round in rounds:
        items = round.split(",")
        for item in items:
            match = not_none(round_regex.match(item.strip()))
            mins[match.group(2)] = max(mins[match.group(2)], int(match.group(1)))
    power = reduce(lambda a, b: a * b, mins.values())
    sum += power


print(sum)
