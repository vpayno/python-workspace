""" Rich Module Demo """

import time

from rich import print  # pylint: disable=redefined-builtin
from rich import traceback
from rich.console import Console
from rich.theme import Theme

# ruff: noqa: W0622


traceback.install(show_locals=True)


def demo_console() -> None:
    """Rich Console demo"""

    console = Console()

    console.print(
        """
[green underline]Green[/]
[blue italic]Blue[/]
[red bold]Red[/]
"""
    )
    print()

    console.print("rich console print demo\n")

    console.print(
        """
        [green underline]Green[/]
        [blue italic]Blue[/]
        [red bold]Red[/]
        """
    )
    print()

    console.print("[green underline]Green[/] [blue italic]Blue[/] [red bold]Red[/]\n")
    console.print("[#00ffff]Hello[/] [#ff00ff]World[/][#ffff00]![/]\n")
    console.print("[black on bright_yellow]Using a yellow highlighter![/]\n")
    console.print("[red on green reverse]Red fg on Green gb reversed[/]\n")
    console.print("[red blink]blinking red fg[/]\n")

    print("\n\n")


def demo_theme() -> None:
    """Rich Console Theme Demo"""
    custom_theme: Theme = Theme(
        {"title": "bold underline green", "info": "bold cyan", "warning": "magenta", "danger": "bold red"}
    )

    console = Console(theme=custom_theme)

    console.print("rich console theme demo\n", style="title")
    console.print("informational message", style="info")
    console.print("cautionary message", style="warning")
    console.print("alert message", style="danger")

    print("\n\n")


def demo_log() -> None:
    """Rich Console Log Demo"""

    custom_theme: Theme = Theme(
        {"title": "bold underline green", "info": "bold cyan", "warning": "magenta", "danger": "bold red"}
    )

    console = Console(theme=custom_theme)

    console.print("rich console log demo\n", style="title")

    console.log("informational message", style="info")
    console.log("cautionary message", style="warning")
    time.sleep(1)
    console.log("alert message", style="danger")

    print("\n\n")


def demo_runtime_error() -> None:
    """Rich RuntimeError Traceback Demo"""

    custom_theme: Theme = Theme(
        {
            "title": "bold underline green",
            "subtitle": "bold green",
            "info": "bold cyan",
            "warning": "magenta",
            "danger": "bold red",
        }
    )

    console = Console(theme=custom_theme)

    console.print("rich runtime error demo\n", style="title")

    try:
        raise RuntimeError("Intentionally failing")
    except RuntimeError:  # or Exception
        import traceback as py_tb  # pylint: disable=import-outside-toplevel

        console.print("Using Python's built-in traceback\n", style="subtitle")
        print(py_tb.format_exc())
        print()

        console.print("Using Rich's traceback\n", style="subtitle")
        console.print_exception(show_locals=True)


def main() -> None:
    """Main Function"""

    demo_console()
    demo_theme()
    demo_log()
    demo_runtime_error()


if __name__ == "__main__":  # pragma: no cover
    main()
