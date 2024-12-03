import re
from utils.file import read_file

contents = read_file(__file__, "input")
contents.strip().splitlines()
result: list[tuple[str, str]] = re.findall(r'mul\((\d+),(\d+)\)', contents)
total = sum([int(a) * int(b) for a, b in result])
print(total)
