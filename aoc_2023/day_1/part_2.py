import re
from utils.file import read_file
from typing import TypeVar, Optional


text_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

T = TypeVar("T")


def not_none(a: Optional[T]) -> T:
    if a is None:
        raise Exception("a is None")
    return a


contents = read_file(__file__, "input")
lines = contents.split("\n")
sum = 0
keys = "|".join(text_digits.keys())
pat = r"(\d|" + keys + ")"
regex = re.compile(pat)
pat_end = r".*" + pat + r".*?$"
regex = re.compile(pat)
regex_end = re.compile(pat_end)
for line in lines:
    if not line:
        continue
    first = not_none(regex.search(line)).group(1)
    last = not_none(regex_end.search(line)).group(1)
    num = int(
        (text_digits[first] if first in text_digits else first)
        + (text_digits[last] if last in text_digits else last)
    )
    sum += num


print(sum)
