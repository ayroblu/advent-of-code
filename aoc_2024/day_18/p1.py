from utils.file import read_input

contents = read_input(__file__).strip()

lines = contents.splitlines()

maxn = 70

dropped = 1024
affected = lines[:dropped]

type Point = tuple[int, int]
corrupted = set[Point]()
for line in affected:
    r, c = map(int, line.split(","))
    corrupted.add((r, c))


def run() -> int:
    seen = set[Point]()
    poss = [(0, 0)]
    end = (maxn, maxn)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = 0
    while len(poss) > 0:
        dist += 1
        next_poss: list[Point] = []
        for r, c in poss:
            for dr, dc in dirs:
                r1, c1 = r + dr, c + dc
                if (r1, c1) == end:
                    return dist

                if not (0 <= r1 <= maxn):
                    continue
                if not (0 <= c1 <= maxn):
                    continue
                if (r1, c1) in corrupted:
                    continue

                if (r1, c1) in seen:
                    continue
                seen.add((r1, c1))

                next_poss.append((r1, c1))
        poss = next_poss
    assert False


print(run())
