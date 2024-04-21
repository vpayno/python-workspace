"""learn_enum tests"""

import learn_enum.color
import learn_enum.intcolor
import learn_enum.namedcolor
import learn_enum.number
import learn_enum.weekday


def test_color() -> None:
    red: learn_enum.color.Color = learn_enum.color.Color.RED
    blue: learn_enum.color.Color = learn_enum.color.Color.BLUE

    assert red.value < blue.value


def test_intcolor() -> None:
    red: learn_enum.intcolor.IntColor = learn_enum.intcolor.IntColor.RED
    blue: learn_enum.intcolor.IntColor = learn_enum.intcolor.IntColor.BLUE

    assert red < blue


def test_namedcolor() -> None:
    red: learn_enum.namedcolor.NamedColor = learn_enum.namedcolor.NamedColor.RED
    blue: learn_enum.namedcolor.NamedColor = learn_enum.namedcolor.NamedColor.BLUE

    assert red.value[0] < blue.value[0]


def test_number() -> None:
    one: learn_enum.number.Number = learn_enum.number.Number.ONE
    two: learn_enum.number.Number = learn_enum.number.Number.TWO

    assert one < two


def test_weekday() -> None:
    monday: learn_enum.weekday.Weekday = learn_enum.weekday.Weekday.MONDAY
    sunday: learn_enum.weekday.Weekday = learn_enum.weekday.Weekday.SUNDAY

    assert monday.number < sunday.number
