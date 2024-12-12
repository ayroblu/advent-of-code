from itertools import chain
from typing import Union

from utils.file import read_input

contents = read_input(__file__).strip()

items = contents.split(" ")


def rules(item: str) -> Union[str, list[str]]:
    if item == "0":
        return ["1"]
    if len(item) % 2 == 0:
        return [str(int(item[: len(item) // 2])), str(int(item[len(item) // 2 :]))]
    return [str(int(item) * 2024)]


flatten = chain.from_iterable
for iter in range(25):
    items = list(flatten(map(rules, items)))

print(len(items))
