from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.split("\n")
max = 0
current = 0
for line in lines:
    if not line:
        current = 0
        continue
    current += int(line)
    if current > max:
        max = current


print(max)
