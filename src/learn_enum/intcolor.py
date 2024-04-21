"""Enum IntColor Demo"""

from enum import CONTINUOUS, UNIQUE, IntFlag, auto, verify


@verify(CONTINUOUS, UNIQUE)
class IntColor(IntFlag):
    RED = 0
    BLUE = auto()
    GREEN = auto()


def intcolor_demo() -> None:
    """IntColor Demo Function"""

    print()

    print("Enum Color using IntFlag:\n")
    for int_color in IntColor:
        print(f"{int_color}")
        print(f" name: {int_color.name}")
        print(f"value: {int_color.value}")
        print()
