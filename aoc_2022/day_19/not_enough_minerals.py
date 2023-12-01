import re
from dataclasses import dataclass

from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.split("\n")


@dataclass
class Blueprint:
    id: int
    ore_cost_ore: int
    clay_cost_ore: int
    obsidian_cost_ore: int
    obsidian_cost_clay: int
    geode_cost_ore: int
    geode_cost_obsidian: int


def scenario(blueprint: Blueprint):
    ore = 0
    clay = 0
    obsidian = 0
    geode = 0
    ore_robots = 1
    clay_robots = 0
    obsidian_robots = 0
    geode_robots = 0
    for _ in range(24):
        new_ore_robot = 0
        new_clay_robot = 0
        new_obsidian_robot = 0
        new_geode_robot = 0
        if (
            blueprint.geode_cost_ore <= ore
            and blueprint.geode_cost_obsidian <= obsidian
        ):
            ore -= blueprint.geode_cost_ore
            obsidian -= blueprint.geode_cost_obsidian
            new_geode_robot += 1
        if blueprint.obsidian_cost_ore <= ore and blueprint.obsidian_cost_clay <= clay:
            ore -= blueprint.obsidian_cost_ore
            clay -= blueprint.obsidian_cost_clay
            new_obsidian_robot += 1
        if (
            blueprint.clay_cost_ore <= ore
            and blueprint.obsidian_cost_clay > clay + clay_robots
        ):
            ore -= blueprint.clay_cost_ore
            new_clay_robot += 1
        if (
            blueprint.ore_cost_ore <= ore
            and blueprint.obsidian_cost_ore + blueprint.geode_cost_ore
            > ore + ore_robots
        ):
            ore -= blueprint.ore_cost_ore
            new_ore_robot += 1

        # for each robot, collect 1 type
        # 1: if you have the ore and obsidian, should you make geode robot
        #   Always true
        # 2: if you have the ore and clay, should you make obsidian robot
        #   probably true?
        # 3: if you have the ore, should you make clay robot
        # 4: if you have the ore, should you make ore robot

        ore += ore_robots
        clay += clay_robots
        obsidian += obsidian_robots
        geode += geode_robots

        ore_robots += new_ore_robot
        clay_robots += new_clay_robot
        obsidian_robots += new_obsidian_robot
        geode_robots += new_geode_robot
    return geode


pat = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
regex = re.compile(pat)
quality = 0
for line in lines:
    if not line:
        continue
    match = regex.match(line)
    if not match:
        print("fail", line)
        continue
    blueprint = Blueprint(
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        int(match.group(4)),
        int(match.group(5)),
        int(match.group(6)),
        int(match.group(7)),
    )
    geodes = scenario(blueprint)
    quality += geodes * blueprint.id

a = scenario(Blueprint(1, 4, 2, 3, 14, 2, 7))
b = scenario(Blueprint(2, 2, 3, 3, 8, 3, 12))
print(a, b, (a * 1) + b * 2)

print("Quality", quality)

# print(max)
