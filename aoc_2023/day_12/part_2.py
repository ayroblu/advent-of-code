from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.split("\n")
sum = 0

for line in lines:
    spring, meta_str = line.split()
    spring = "?".join([spring] * 5)
    meta: list[int] = list(map(int, meta_str.split(",")))
    meta: list[int] = meta * 5

    cache: dict[tuple[int, int], int] = {(0, 0): 1}
    for i, char in enumerate(spring):
        new_cache: dict[tuple[int, int], int] = {}
        is_last = i == len(spring) - 1

        def cache_set(key: tuple[int, int], count: int):
            if key in new_cache:
                count += new_cache[key]
            new_cache[key] = count

        for (prev, index), count in cache.items():

            def handle(char: str):
                """Handle "." and "#" characters in a DP fashion"""
                if char == ".":
                    if prev == 0:
                        cache_set((prev, index), count)
                    elif index < len(meta) and prev == meta[index]:
                        cache_set((0, index + 1), count)
                elif char == "#" and index < len(meta):
                    next = (prev + 1, index)
                    if is_last and next[0] == meta[index]:
                        cache_set((0, index + 1), count)
                    elif next[0] <= meta[index]:
                        cache_set(next, count)

            if char == "?":
                handle(".")
                handle("#")
            else:
                handle(char)
        cache = new_cache
    sum += cache[(0, len(meta))]

print(sum)
