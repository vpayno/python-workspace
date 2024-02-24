""" Toml Workspace/Demo """

import tomllib
from pprint import pprint

from rich.traceback import install

install()  # setup rich


def load_toml() -> dict:
    """Load TOML data from file"""

    with open("src/learn_toml/config.toml", "rb") as f:
        toml_data: dict = tomllib.load(f)

        return toml_data


def main() -> None:
    """Runs the toml demos"""

    # Load Toml data
    data: dict = load_toml()
    pprint(data, sort_dicts=False)


if __name__ == "__main__":  # pragma: no cover
    main()
