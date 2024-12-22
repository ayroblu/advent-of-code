from utils.file import read_input

contents = read_input(__file__)

lines = map(int, contents.splitlines())


def secret(n: int) -> int:
    n ^= n * 64
    n %= 16777216
    n ^= n // 32
    n %= 16777216
    n ^= n * 2048
    n %= 16777216
    return n


total = 0
for n in lines:
    for i in range(2000):
        n = secret(n)
    total += n

print(total)
