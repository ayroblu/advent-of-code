import re
from dataclasses import dataclass
from typing import Callable

from utils.file import read_input

contents = read_input(__file__)


@dataclass
class Monkey:
    idx: int
    items: list[int]
    op: Callable[[int], int]
    div: int
    true_monkey: int
    false_monkey: int
    inspections: int = 0


pat = re.compile(
    r"""Monkey (\d+):
  Starting items: (.*)
  Operation: new = old (.) (\d+|old)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""
)


def handle_op(op: str, op_value: str) -> Callable[[int], int]:
    def func(old: int) -> int:
        value = old if op_value == "old" else int(op_value)
        if op == "*":
            return old * value
        elif op == "/":
            return old // value
        elif op == "+":
            return old + value
        elif op == "-":
            return old - value

        raise Exception("unreachable")

    return func


monkeys: list[Monkey] = []
for match in re.finditer(pat, contents):
    idx, items, op, op_value, div, true_monkey, false_monkey = match.groups()
    monkey = Monkey(
        int(idx),
        [int(i) for i in items.split(", ")],
        handle_op(op, op_value),
        int(div),
        int(true_monkey),
        int(false_monkey),
    )
    monkeys.append(monkey)

for i in range(20):
    for monkey in monkeys:
        monkey.inspections += len(monkey.items)
        for item in monkey.items:
            value = monkey.op(item) // 3
            if value % monkey.div == 0:
                monkeys[monkey.true_monkey].items.append(value)
            else:
                monkeys[monkey.false_monkey].items.append(value)
        monkey.items = []

inspections = [monkey.inspections for monkey in monkeys]
inspections.sort()
a, b = inspections[-2:]
print(a * b)
