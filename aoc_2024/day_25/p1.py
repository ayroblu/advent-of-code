from typing import cast

from utils.file import read_input

contents = read_input(__file__)

items_str = contents.split("\n\n")
items = [item.splitlines() for item in items_str]

type Lock = tuple[int, int, int, int, int]
locks = list[Lock]()
keys = list[Lock]()


def count_key(item: list[str]) -> Lock:
    rows = list(zip(*item))
    return cast(Lock, [row.count("#") - 1 for row in rows])


for item in items:
    if item[0][0] == "#":
        locks.append(count_key(item))
    else:
        keys.append(count_key(item))


counts = 0
for lock in locks:
    for key in keys:
        if all(l + k <= 5 for l, k in zip(lock, key)):
            counts += 1

print(counts)
