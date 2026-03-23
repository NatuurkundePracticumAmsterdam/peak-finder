import subprocess
from importlib.resources import files


def main():
    notebook = files("peak_finder_notebook").joinpath("peak-finder.ipynb")
    subprocess.run(["jupyter", "lab", str(notebook)], check=True)
