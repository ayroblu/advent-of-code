from typing import Union

from utils.file import read_file

contents = read_file(__file__, "input")
problems = contents.split("\n\n")
horizontal_total = 0
vertical_total = 0


def equal_with_err(l1: str, l2: str, err: int) -> int:
    for c1, c2 in zip(l1, l2):
        if c1 != c2:
            err += 1
        if err > 1:
            break
    return err


def get_line(grid: list[str]) -> Union[int, None]:
    for i in range(1, len(grid)):
        slice1 = grid[:i]
        slice2 = grid[i:]
        err = 0
        for l1, l2 in zip(slice1, reversed(slice2)):
            err = equal_with_err(l1, l2, err)
            if err > 1:
                break
        if err == 1:
            return i


for i, problem in enumerate(problems):
    grid = [line for line in problem.splitlines()]
    line = get_line(grid)
    if line is not None:
        horizontal_total += line
        continue

    grid_t = ["".join(line) for line in zip(*grid)]
    line = get_line(grid_t)
    if line is not None:
        vertical_total += line
        continue

    raise Exception("no")

result = vertical_total + 100 * horizontal_total

print(result)
