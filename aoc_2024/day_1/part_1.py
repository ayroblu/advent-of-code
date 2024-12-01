import re
from utils.file import read_file


contents = read_file(__file__, "input")
lines = contents.strip().split("\n")
all = [(int(x) for x in re.split(r' +', line)) for line in lines]
left, right = [list(x) for x in zip(*all)]
left.sort()
right.sort()
sum = 0
for (a, b) in zip(left, right):
    sum += abs(a - b)


print(sum)

