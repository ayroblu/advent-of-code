from typing import TypeVar, Optional

T = TypeVar("T")


def not_none(a: Optional[T]) -> T:
    if a is None:
        raise Exception("a is None")
    return a
