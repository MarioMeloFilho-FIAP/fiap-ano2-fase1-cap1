"""
Utility helpers for filesystem and downloads.
"""

from __future__ import annotations

import re
from pathlib import Path

import requests


def ensure_dir(path: str | Path) -> Path:
    """
    Ensure a directory exists and return it as Path.
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def sanitize_filename(value: str) -> str:
    """
    Convert arbitrary text into a safe filename.
    """
    safe = re.sub(r"[^a-zA-Z0-9._-]+", "_", value.strip())
    return safe.strip("_") or "file"


def download_file(url: str, destination: str | Path, timeout: int = 60) -> Path:
    """
    Download a file to a local destination.

    Parameters
    ----------
    url : str
        Source URL.
    destination : str | Path
        Output file path.
    timeout : int
        Request timeout in seconds.

    Returns
    -------
    Path
        Downloaded file path.
    """
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)

    with requests.get(url, stream=True, timeout=timeout) as response:
        response.raise_for_status()
        with destination.open("wb") as file_obj:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file_obj.write(chunk)

    return destination
