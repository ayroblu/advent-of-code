from utils.file import read_input

contents = read_input(__file__)

x = [1]
skip = False
for line in contents.splitlines():
    last = x[-1]
    if line == "noop":
        if not skip:
            x.append(last)
        skip = False
    if line.startswith("addx"):
        _, v = line.split()
        num = int(v)
        if not skip:
            x.append(last)
        x.append(last)
        x.append(last + num)
        skip = True

cycle = [20, 60, 100, 140, 180, 220]
result = [c * x[c] for c in cycle]
print(sum(result))
