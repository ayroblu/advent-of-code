from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__).strip()

items = contents.split(" ")


def rules(item: str) -> list[str]:
    if item == "0":
        return ["1"]
    if len(item) % 2 == 0:
        return [str(int(item[: len(item) // 2])), str(int(item[len(item) // 2 :]))]
    return [str(int(item) * 2024)]


total_iter = 75
todo = defaultdict[str, int](int)
for item in items:
    todo[item] += 1

total = 0
for iter in range(total_iter):
    next: defaultdict[str, int] = defaultdict(int)
    for item, count in todo.items():
        result = rules(item)
        for res in result:
            next[res] += count
    todo = next
    total = sum(next.values())

print(total)
