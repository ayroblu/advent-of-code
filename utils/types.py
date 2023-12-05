from typing import Optional

def not_none[T](a: Optional[T]) -> T:
    if a is None:
        raise Exception("a is None")
    return a
