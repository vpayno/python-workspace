"""Enum Number Demo"""

from enum import CONTINUOUS, UNIQUE, IntEnum, auto, verify


@verify(CONTINUOUS, UNIQUE)
class Number(IntEnum):
    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()


def intenum_demo() -> None:
    """IntEnum Demo Function"""

    print()

    print("Enum Number using IntEnum:\n")
    for number in Number:
        print(f"{number}")
        print(f" name: {number.name}")
        print(f"value: {number.value}")
        print()
