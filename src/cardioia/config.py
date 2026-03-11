"""
utilities loader.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_yaml_config(path: str | Path) -> dict[str, Any]:
    """
    Load a YAML configuration file.

    Parameters
    ----------
    path : str | Path
        Path to the YAML file.

    Returns
    -------
    dict[str, Any]
        Parsed YAML content.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    ValueError
        If the file is empty or invalid.
    """
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as stream:
        data = yaml.safe_load(stream)

    if not data:
        raise ValueError(f"Configuration file is empty or invalid: {config_path}")

    return data
