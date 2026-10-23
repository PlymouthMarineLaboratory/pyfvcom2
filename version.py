"""Compatibility access to the package version.

The authoritative version is kept in :mod:`pyfvcom2.version`, because that
is the module used by the build configuration.  Keep this module for tools
that expect a top-level ``version.py`` file.
"""

from pathlib import Path
from runpy import run_path


_package_version = run_path(
    str(Path(__file__).with_name("pyfvcom2") / "version.py")
)
version = _package_version["short_version"]

__all__ = ["version"]
