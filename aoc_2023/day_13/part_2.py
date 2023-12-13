from typing import Union

from utils.file import read_file

contents = read_file(__file__, "input")
problems = contents.split("\n\n")
horizontal_total = 0
vertical_total = 0


def equal_with_err(l1: list[str], l2: list[str], err: int) -> int:
    for c1, c2 in zip(l1, l2):
        if c1 != c2:
            err += 1
        if err > 1:
            break
    return err


def get_line(grid: list[list[str]]) -> Union[int, None]:
    for i in range(len(grid))[:0:-1]:
        if i % 2 == 0:
            continue
        err = 0
        for i2 in range(0, len(grid)):
            if i2 > i - i2:
                break
            err = equal_with_err(grid[i2], grid[i - i2], err)
            if err > 1:
                break
        if err == 1:
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
