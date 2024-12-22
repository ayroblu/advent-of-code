from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__)

lines = contents.splitlines()

keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["x", "0", "A"],
]
dirpad = [
    ["x", "^", "A"],
    ["<", "v", ">"],
]
keypad_loc = dict(
    [(char, (r, c)) for r, row in enumerate(keypad) for c, char in enumerate(row)]
)
dirpad_loc = dict(
    [(char, (r, c)) for r, row in enumerate(dirpad) for c, char in enumerate(row)]
)


def get_keypad_steps(f_char: str, to: str) -> list[str]:
    fr, fc = keypad_loc[f_char]
    tr, tc = keypad_loc[to]
    if fc == 0 and tr == 3:
        # ignore current_dir, there's only one way
        return [(tc - fc) * ">" + (tr - fr) * "v" + "A"]
    if fr == 3 and tc == 0:
        # ignore current_dir, there's only one way
        return [(fr - tr) * "^" + (fc - tc) * "<" + "A"]
    dh = tc - fc
    dv = tr - fr
    h = dh * ">" if dh > 0 else abs(dh) * "<"
    v = dv * "v" if dv > 0 else abs(dv) * "^"
    if dh > 0 and f_char == ">" or dh < 0 and f_char == "<":
        return [h + v + "A"]
    if dv > 0 and f_char == "v" or dv < 0 and f_char == "^":
        return [v + h + "A"]
    if dv == 0:
        return [h + "A"]
    if dh == 0:
        return [v + "A"]
    return [v + h + "A", h + v + "A"]


def get_dirpad_steps(f_char: str, to: str) -> list[str]:
    fr, fc = dirpad_loc[f_char]
    tr, tc = dirpad_loc[to]
    if fc == 0 and tr == 0:
        # ignore current_dir, there's only one way
        return [(tc - fc) * ">" + (fr - tr) * "^" + "A"]
    if fr == 0 and tc == 0:
        # ignore current_dir, there's only one way
        return [(tr - fr) * "v" + (fc - tc) * "<" + "A"]
    dh = tc - fc
    dv = tr - fr
    h = dh * ">" if dh > 0 else abs(dh) * "<"
    v = dv * "v" if dv > 0 else abs(dv) * "^"
    if dh > 0 and f_char == ">" or dh < 0 and f_char == "<":
        return [h + v + "A"]
    if dv > 0 and f_char == "v" or dv < 0 and f_char == "^":
        return [v + h + "A"]
    if dv == 0:
        return [h + "A"]
    if dh == 0:
        return [v + "A"]

    # debatable
    if to == "A":
        return [v + h + "A"]
    if f_char == "^":
        return [v + h + "A"]
    if f_char == ">":
        return [h + v + "A"]
    if f_char == "A" and to == "v":
        return [h + v + "A"]
    # print(f_char, to)
    # assert False
    return [v + h + "A", h + v + "A"]


graph: dict[tuple[str, str], list[str]] = {}


def get_results(text: str) -> dict[tuple[str, str], int]:
    counts: dict[tuple[str, str], int] = {}
    for i, char in enumerate(text):
        if (text[i - 1], char) in counts:
            counts[text[i - 1], char] += 1
            continue
        counts[text[i - 1], char] = 1

        if (text[i - 1], char) not in graph:
            options = get_dirpad_steps(text[i - 1], char)
            graph[text[i - 1], char] = options
    return counts


def get_min_dirpad_steps(text: str) -> int:
    results: list[dict[str, int]] = [defaultdict(int)]
    for i, char in enumerate(text):
        options = get_keypad_steps(text[i - 1], char)
        results1 = list[dict[str, int]]()
        for result in results:
            for option in options:
                next_result = result.copy()
                next_result[option] += 1
                results1.append(next_result)
        results = results1
    # print([dict(result) for result in results])

    for i in range(25):
        next_results: list[dict[str, int]] = []
        for result in results:
            results1 = [defaultdict[str, int](int)]
            for text, prev_count in result.items():
                result_counts = get_results(text)
                for key, count in result_counts.items():
                    if len(graph[key]) == 1:
                        for option in graph[key]:
                            for result1 in results1:
                                result1[option] += count * prev_count
                    else:
                        next_result1: list[dict[str, int]] = []
                        for option in graph[key]:
                            for result1 in results1:
                                next_result = result1.copy()
                                next_result[option] += count * prev_count
                                next_result1.append(next_result)
                        results1 = next_result1
            next_results.extend(results1)
        # print([dict(result) for result in next_results])
        results = next_results

    return min(
        sum(len(key) * count for key, count in result.items()) for result in results
    )


total = 0
for line in lines:
    allsteps = get_min_dirpad_steps(line)
    print(line, allsteps)
    total += allsteps * int(line[:-1])
print(total)
