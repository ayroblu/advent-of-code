import re

from utils.file import read_file
from utils.types import not_none

contents = read_file(__file__, "input")
lines = contents.split("\n")

max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

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
    is_possible = True
    for round in rounds:
        items = round.split(",")
        for item in items:
            match = not_none(round_regex.match(item.strip()))
            if max[match.group(2)] < int(match.group(1)):
                is_possible = False
    if is_possible:
        sum += id


print(sum)
