"""Enum Color Demo"""

from enum import NAMED_FLAGS, UNIQUE, Flag, auto, verify


@verify(NAMED_FLAGS, UNIQUE)
class Color(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()


def color_demo() -> None:
    """Color Demo Function"""

    print()

    print("Enum Color using Flag:\n")
    for color in Color:
        print(f"{color}")
        print(f" name: {color.name}")
        print(f"value: {color.value}")
        print()
