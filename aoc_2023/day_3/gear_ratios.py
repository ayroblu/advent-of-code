import re

from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.split("\n")

sum = 0
regex = re.compile(r"[^.\d]")
digits_regex = re.compile(r"\d+")
for index, line in enumerate(lines):
    if not line:
        continue
    matches = digits_regex.finditer(line)
    for match in matches:
        working_num = match.group()
        start_index, end_index = match.span()
        if (
            (
                index > 0
                and regex.search(
                    lines[index - 1][
                        max(start_index - 1, 0) : min(end_index + 1, len(line))
                    ]
                )
            )
            or (start_index > 0 and regex.search(line[start_index - 1]))
            or (end_index < len(line) - 1 and regex.search(line[end_index]))
            or (
                index < len(lines) - 1
                and regex.search(
                    lines[index + 1][
                        max(start_index - 1, 0) : min(end_index + 1, len(line))
                    ]
                )
            )
        ):
            sum += int(working_num)


print(sum)
