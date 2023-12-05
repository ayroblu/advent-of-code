import re
from dataclasses import dataclass

from utils.file import read_file
from utils.types import not_none

contents = read_file(__file__, "input")
almanac_regex = re.compile(
    r"""
seeds: (.*)

seed-to-soil map:
([\s\S]*)

soil-to-fertilizer map:
([\s\S]*)

fertilizer-to-water map:
([\s\S]*)

water-to-light map:
([\s\S]*)

light-to-temperature map:
([\s\S]*)

temperature-to-humidity map:
([\s\S]*)

humidity-to-location map:
([\s\S]*)
""".strip(),
    re.MULTILINE,
)
match = not_none(almanac_regex.match(contents))
seeds = map(lambda x: int(x), match.group(1).strip().split(" "))


@dataclass
class Mapper:
    dest: int
    source: int
    num: int


def parse_maps(text: str):
    lines = text.strip().splitlines()
    result: list[Mapper] = []
    for line in lines:
        dest, source, num = line.split(" ")
        result.append(Mapper(int(dest), int(source), int(num)))
    return result


maps = [parse_maps(match.group(i)) for i in range(2, 9)]
min = None
for seed in seeds:
    pos = seed
    for map in maps:
        for mapper in map:
            if mapper.source <= pos < mapper.source + mapper.num:
                pos += mapper.dest - mapper.source
                break
    if min is None or min > pos:
        min = pos


print(min)
