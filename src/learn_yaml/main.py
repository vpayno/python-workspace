""" Yaml Workspace/Demo """

from pprint import pprint
from typing import Any

import ruyaml
import yaml
from rich import pretty
from rich import print as rprint
from rich import traceback

traceback.install()
pretty.install()


def load_yaml() -> dict[Any, Any]:
    """Load Yaml data from a file"""

    print("Reading config file from file.")
    with open("src/learn_yaml/config.yaml", "rb") as f:
        yaml_data: dict[Any, Any] = yaml.safe_load(f)

        return yaml_data


def save_yaml(data: dict[Any, Any]) -> None:
    """Save Yaml data to a file"""

    print("Writing config file to file.")

    if data is None:
        data = {}

    data["newkey"] = "new value"

    print(data)
    print()

    with open("/tmp/pyyaml.yaml", "wb") as f:
        yaml.dump(
            data,
            stream=f,
            encoding="utf-8",
            explicit_start=True,
            explicit_end=None,
            version=None,
            tags=None,
            indent=True,
            width=4,
            allow_unicode=True,
            line_break=None,
        )

    with open("/tmp/ruyaml.yaml", "wb") as f:
        ruyaml.dump(
            data,
            stream=f,
            encoding="utf-8",
            explicit_start=True,
            explicit_end=None,
            version=None,
            tags=None,
            indent=True,
            width=4,
            allow_unicode=True,
            line_break=None,
        )

    with open("/tmp/pyyaml.yaml", "r") as f:
        print("PyYaml Output file:")
        for line in f.readlines():
            print(line.rstrip())

    print()

    with open("/tmp/ruyaml.yaml", "r") as f:
        print("RuYaml Output file:")
        for line in f.readlines():
            print(line.rstrip())

    print()


def main() -> None:
    """Runs the yaml demos"""

    # Load Toml data
    data: dict = load_yaml()

    save_yaml(data)
    print()

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
