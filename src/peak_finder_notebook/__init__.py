import os
import pathlib
from importlib.resources import files

NOTEBOOK = "peak-finder.ipynb"


def copy_from_package_if_missing(resource: str) -> None:
    dest = pathlib.Path.cwd() / resource
    if not dest.exists():
        source = files("peak_finder_notebook").joinpath(resource)
        dest.write_bytes(source.read_bytes())


def main():
    copy_from_package_if_missing(NOTEBOOK)
    copy_from_package_if_missing("example-datafile.csv")
    os.execvp("jupyter", ["jupyter", "lab", NOTEBOOK])
