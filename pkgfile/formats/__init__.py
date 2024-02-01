"""
"""

from pathlib import Path

from importlib.metadata import distribution

from .. import _package


def format_by_version(version: str = "1.0") -> Path:
    """Return the path for a format with the specified version."""
    dist = distribution(_package)

    return dist.locate_file(f"format-{version}.json")
