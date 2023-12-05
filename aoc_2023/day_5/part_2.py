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
seeds_raw = list(map(lambda x: int(x), match.group(1).strip().split(" ")))


@dataclass(eq=True, frozen=True)
class Seed:
    start: int
    length: int

    def __repr__(self):
        return f"({self.start}, {self.length})"


seeds = [Seed(seeds_raw[i], seeds_raw[i + 1]) for i in range(0, len(seeds_raw), 2)]


@dataclass
class Mapper:
    dest: int
    source: int
    length: int


def parse_maps(text: str):
    lines = text.strip().splitlines()
    result: list[Mapper] = []
    for line in lines:
        dest, source, num = line.split(" ")
        result.append(Mapper(int(dest), int(source), int(num)))
    result.sort(key=lambda x: x.source)
    return result


def split_seeds_by_sorted_mapper(
    seed: Seed, sorted_mappers: list[Mapper]
) -> list[Seed]:
    result: list[Seed] = []
    last_index = seed.start
    for mapper in sorted_mappers:
        if last_index < mapper.source:
            last_index = mapper.source
            result.append(
                Seed(seed.start, min(seed.length, mapper.source - seed.start))
            )
        if mapper.source >= seed.start + seed.length:
            last_index = mapper.source
            break
        if mapper.source <= last_index < mapper.source + mapper.length:
            result.append(
                Seed(
                    last_index + (mapper.dest - mapper.source),
                    min(
                        seed.start + seed.length - last_index,
                        mapper.source + mapper.length - last_index,
                    ),
                )
            )
            last_index = mapper.source + mapper.length
    if last_index < seed.start + seed.length:
        result.append(Seed(last_index, seed.start + seed.length - last_index))
    return result


maps = [parse_maps(match.group(i)) for i in range(2, 9)]
min_value = None
for seed in seeds:
    variants = [seed]
    for map in maps:
        variants: list[Seed] = [
            item
            for variant in variants
            for item in split_seeds_by_sorted_mapper(variant, map)
        ]

    for variant in variants:
        if min_value is None or min_value > variant.start:
            min_value = variant.start


print(min_value)
