from utils.file import read_input

contents = read_input(__file__)
# contents = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
##....###..
##OO..#...."""

stacks = list(map(list, contents.splitlines()))


def cycle(stacks: list[list[str]]) -> list[list[str]]:
    for _ in range(4):
        stacks = list(map(list, zip(*stacks)))
        for line in stacks:
            for i, char in enumerate(line):
                if char == "O":
                    idx = i
                    for idx in range(i, -1, -1):
                        if idx == 0 or line[idx - 1] != ".":
                            break
                    if idx != i:
                        line[idx] = "O"
                        line[i] = "."
        stacks = [list(reversed(a)) for a in stacks]
    return stacks


seen: list[list[list[str]]] = []
for i in range(1_000_000_000):
    stacks = cycle(stacks)
    layout = "\n".join(map(lambda x: "".join(x), stacks))
    # print(layout)
    # print("")
    if stacks in seen:
        index = seen.index(stacks)
        diff = len(seen) - index
        offset = (1_000_000_000 - index) % diff
        stacks = seen[index + offset - 1]
        break
    seen.append(stacks)

# imagine 12 and 17 are matches, 1_000_000_000 would be (1e9 - 12) % (17-12)
# 12 + 5*x > 1e9
# (1e9 - 12) / 5

sum = 0
for i, line in enumerate(stacks):
    for char in line:
        if char == "O":
            sum += len(stacks) - i

print(sum)
