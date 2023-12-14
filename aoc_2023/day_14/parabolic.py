from utils.file import read_input

contents = read_input(__file__)

stacks = list(map(list, zip(*contents.splitlines())))
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
sum = 0
for line in stacks:
    for i, char in enumerate(line):
        if char == "O":
            sum += len(line) - i

print(sum)
