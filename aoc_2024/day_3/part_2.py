import re
from utils.file import read_file

contents = read_file(__file__, "input")
contents.strip().splitlines()
result: list[tuple[str, str, str, str]] = re.findall(r'(?:mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\))', contents)
total = 0
enabled = True
for a, b, do, dont in result:
    if do:
        enabled = True
        continue
    if dont:
        enabled = False
        continue
    if enabled:
        total += int(a) * int(b)
print(total)
