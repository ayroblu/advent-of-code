from utils.file import read_input

contents = read_input(__file__).strip()

lines = contents.splitlines()

start = (0, 0)
end = (0, 0)
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "S":
            start = (r, c)
        elif char == "E":
            end = (r, c)

dir = (0, 1)
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
seen = dict[tuple[tuple[int, int], tuple[int, int]], int]()

r, c = start
er, ec = end
start_check: list[
    tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int]
] = [(start, dir, [start], 0)]


def traverse() -> tuple[int, set[tuple[int, int]]]:
    to_check = start_check
    finalcost = int(2e16)
    histories = set[tuple[int, int]]()
    while len(to_check) > 0:
        new_to_check = list[
            tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int]
        ]()
        for (r, c), dir, history, cost in to_check:
            if r == er and c == ec:
                if cost == finalcost:
                    histories.update(set(history))
                elif cost < finalcost:
                    histories = set(history)
                finalcost = min(finalcost, cost)
                continue
            if cost > finalcost:
                continue
            for dr, dc in dirs:
                if (-dr, -dc) == dir:
                    continue
                r1, c1 = r + dr, c + dc
                if lines[r1][c1] == "#":
                    continue
                newcost = cost + (1 if (dr, dc) == dir else 1001)
                if ((r1, c1), (dr, dc)) in seen and newcost > seen[
                    ((r1, c1), (dr, dc))
                ]:
                    continue
                seen[((r1, c1), (dr, dc))] = newcost
                new_to_check.append(((r1, c1), (dr, dc), history + [(r1, c1)], newcost))
        to_check = new_to_check
    return finalcost, histories


cost, histories = traverse()
print(len(histories), cost)
