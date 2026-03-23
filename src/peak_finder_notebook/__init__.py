import pathlib
import subprocess
from importlib.resources import files


def copy_from_package_if_missing(resource: str) -> None:
    dest = pathlib.Path.cwd() / resource
    if not dest.exists():
        source = files("peak_finder_notebook").joinpath(resource)
        dest.write_bytes(source.read_bytes())


def main():
    copy_from_package_if_missing("peak-finder.ipynb")
    copy_from_package_if_missing("example-datafile.csv")
    subprocess.run(["jupyter", "lab", "peak-finder.ipynb"], check=True)
