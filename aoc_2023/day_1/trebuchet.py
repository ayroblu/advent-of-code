import re
from utils.file import read_file


def is_digit(str: str) -> bool:
    return regex.match(str) is not None


contents = read_file(__file__, "input")
lines = contents.split("\n")
sum = 0
pat = r"^\d$"
regex = re.compile(pat)
for line in lines:
    if not line:
        continue
    chars: str = "".join(filter(is_digit, line))
    num = int(chars[0] + chars[-1])
    sum += num


print(sum)
