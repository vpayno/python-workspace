"""Enum NamedColor Demo"""

from enum import Enum


class NamedColor(Enum):
    RED = 0, "Red"
    BLUE = 1, "Blue"
    GREEN = 2, "Green"


def namedcolor_demo() -> None:
    """NamedColor Demo Function"""

    print()

    print("Enum NamedColor using Flag:\n")
    for named_color in NamedColor:
        print(f"{named_color}")
        print(f" name: {named_color.name}")
        print(f"value: {named_color.value}")
        data: tuple[int, str] = named_color.value
        value: int
        name: str
        (value, name) = data
        print(f"data.0: {name}")
        print(f"data.1: {value}")
        print()
