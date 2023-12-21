from typing import Iterable


def mult(items: Iterable[int]) -> int:
    total = 1
    for item in items:
        total *= item
    return total
