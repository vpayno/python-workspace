"""Enum Module Demo"""

from rich.traceback import install as rich_install

from learn_enum.color import color_demo
from learn_enum.intcolor import intcolor_demo
from learn_enum.namedcolor import namedcolor_demo
from learn_enum.number import intenum_demo
from learn_enum.weekday import namedtuple_demo

rich_install(show_locals=True)


def main() -> None:
    """Main Function"""

    color_demo()
    intcolor_demo()
    namedcolor_demo()
    intenum_demo()
    namedtuple_demo()


if __name__ == "__main__":  # pragma: no cover
    main()
