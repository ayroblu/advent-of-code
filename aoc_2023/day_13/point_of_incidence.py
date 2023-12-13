from typing import Union

from utils.file import read_file

contents = read_file(__file__, "input")
problems = contents.split("\n\n")
horizontal_total = 0
vertical_total = 0


def get_line(grid: list[list[str]]) -> Union[int, None]:
    for i in range(len(grid))[:0:-1]:
        if grid[i] == grid[0]:
            if all(
                [l2 == grid[i - 1 - i2] for i2, l2 in enumerate(grid[1 : (i + 1) // 2])]
            ):
                return (i + 1) // 2


for i, problem in enumerate(problems):
    grid = [list(line) for line in problem.splitlines()]
    line = get_line(grid)
    if line is not None:
        horizontal_total += line
        continue

    line = get_line(list(reversed(grid)))
    if line is not None:
        horizontal_total += len(grid) - line
        continue

    line = get_line(list(map(list, zip(*grid))))
    if line is not None:
        vertical_total += line
        continue

    line = get_line(list(reversed(list(map(list, zip(*grid))))))
    if line is not None:
        vertical_total += len(grid[0]) - line
        continue

    raise Exception("no")

result = vertical_total + 100 * horizontal_total

print(result)
