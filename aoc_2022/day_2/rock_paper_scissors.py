from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.split("\n")

rps_map = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}
matrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3],
]


def get_score(key: int) -> int:
    return key + 1


# 1 for rock
# 2 for paper
# 3 for scissors
total_score = 0
for line in lines:
    if not line:
        continue
    opponent, your_choice = line.split(" ")
    score = matrix[rps_map[opponent]][rps_map[your_choice]] + get_score(
        rps_map[your_choice]
    )
    total_score += score


print(total_score)
