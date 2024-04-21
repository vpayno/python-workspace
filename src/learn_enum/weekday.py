"""Enum NamedTuple Demo"""

from collections import namedtuple
from enum import Enum
from typing import NamedTuple

WeekdayT = NamedTuple("WeekdayT", [("number", int), ("name", str), ("abbrv", str)])


# can't figure out how to type the namedtuple below
class Weekday(namedtuple("Weekday", ["number", "name", "abbrv"]), Enum):
    MONDAY = 0, "Monday", "Mon"
    TUESDAY = 1, "Tuesday", "Tue"
    WEDNESDAY = 2, "Wednesday", "Wed"
    THURSDAY = 3, "Thursday", "Thu"
    FRIDAY = 4, "Friday", "Fri"
    SATURDAY = 5, "Saturday", "Sat"
    SUNDAY = 6, "Sunday", "Sun"


def namedtuple_demo() -> None:
    """NamedTuple Demo Function"""

    print()

    print("Enum Weekday using NamedTuples:\n")
    for weekday in Weekday:
        print(f"{weekday}")
        print(f" value: {weekday.value}")
        print(f"number: {weekday.number}")
        print(f"  name: {weekday.name}")
        print(f" abbrv: {weekday.abbrv}")
        print()
