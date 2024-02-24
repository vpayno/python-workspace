""" Yaml Workspace/Demo """

from pprint import pprint
from typing import Any

import yaml
from rich import pretty
from rich import print as rprint
from rich import traceback

traceback.install()
pretty.install()


def load_yaml() -> dict[Any, Any]:
    """Load TOML data from file"""

    with open("src/learn_yaml/config.yaml", "rb") as f:
        yaml_data: dict[Any, Any] = yaml.safe_load(f)

        return yaml_data


def main() -> None:
    """Runs the yaml demos"""

    # Load Toml data
    data: dict = load_yaml()

    print("Using built-in print()\n")
    print(data)
    print()

    print("Using pprint()\n")
    pprint(data, sort_dicts=False)
    print()

    print("Using rich.print()\n")
    rprint(data)
    print()


if __name__ == "__main__":  # pragma: no cover
    main()
