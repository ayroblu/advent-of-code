import re
from dataclasses import dataclass
from typing import Union

from utils.file import read_input

contents = read_input(__file__)


@dataclass
class File:
    size: int


type Directory = dict[str, Union[File, Directory]]

cd_regex = re.compile(r"\$ cd (.*)")
file_regex = re.compile(r"(\d+) ([^\s]+)$")
dir_regex = re.compile(r"dir ([^\s]+)$")
# dir_path: list[str] = []
tree: Directory = {}
current_dir: Directory = tree
for line in contents.splitlines():
    cd_match = cd_regex.match(line)
    if cd_match:
        path: str = cd_match.group(1)
        if path == "/":
            continue
        current_dir = current_dir[path]  # type: ignore
        continue
    file_match = file_regex.match(line)
    if file_match:
        size_str, name = file_match.groups()
        current_dir[name] = File(int(size_str))
        continue
    dir_match = dir_regex.match(line)
    if dir_match:
        name = dir_match.group(1)
        current_dir[name] = {"..": current_dir}

total = 0
threshold = 100000


def get_size(dir: Directory) -> int:
    global total, threshold
    size = 0
    for key, item in dir.items():
        if isinstance(item, File):
            size += item.size
        else:
            if key != "..":
                size += get_size(item)
    if size < threshold:
        total += size
    return size


get_size(tree)
print(total)
