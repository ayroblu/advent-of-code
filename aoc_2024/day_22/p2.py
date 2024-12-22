from collections import defaultdict, deque

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
all_prices = list[dict[tuple[int, int, int, int], int]]()
for n in lines:
    prices = deque([int(str(n)[-1])])
    price_map = dict[tuple[int, int, int, int], int]()
    for i in range(2000):
        n = secret(n)
        price = int(str(n)[-1])
        prices.append(price)
        if len(prices) == 5:
            a, b, c, d, e = prices
            key = b - a, c - b, d - c, e - d
            if key not in price_map:
                price_map[key] = e
            prices.popleft()
    total += n
    all_prices.append(price_map)


def sumdict[K](items: list[dict[K, int]]) -> dict[K, int]:
    acc = defaultdict[K, int](int)
    for item in items:
        for key, value in item.items():
            acc[key] += value
    return acc


total_prices = sumdict(all_prices)
max_price = max(total_prices.values())
print(max_price)
