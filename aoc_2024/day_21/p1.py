from utils.file import read_input

contents = read_input(__file__)

lines = contents.splitlines()

keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["x", "0", "A"]]
dirpad = [["x", "^", "A"], ["<", "v", ">"]]
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
        return [(fr - tr) * "v" + (fc - tc) * "<" + "A"]
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
    return [v + h + "A", h + v + "A"]


def get_min_dirpad_steps(text: str) -> str:
    results = [""]
    for i, char in enumerate(text):
        options = get_keypad_steps(text[i - 1], char)
        results = [prefix + option for option in options for prefix in results]

    for i in range(2):
        next_next_results: list[str] = []
        for text in results:
            next_results = [""]
            for i, char in enumerate(text):
                options = get_dirpad_steps(text[i - 1], char)
                next_results = [
                    prefix + option for option in options for prefix in next_results
                ]
            next_next_results.extend(next_results)
        results = next_next_results

    return min(results, key=lambda x: len(x))


total = 0
for line in lines:
    allsteps = get_min_dirpad_steps(line)
    total += len(allsteps) * int(line[:-1])
print(total)
