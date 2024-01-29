from pprint import pprint

import yaml
from rich.traceback import install

install()  # setup rich


def load_yaml() -> dict:
    """Load TOML data from file"""

    with open("src/learn_yaml/config.yaml", "rb") as f:
        yaml_data = yaml.safe_load(f)

        return yaml_data


def main() -> None:
    # Load Toml data
    data: dict = load_yaml()
    pprint(data, sort_dicts=False)


if __name__ == "__main__":  # pragma: no cover
    main()
