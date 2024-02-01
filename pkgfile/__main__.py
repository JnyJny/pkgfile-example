"""
"""


from importlib.metadata import distribution

from . import _package

from .formats import format_by_version

if __name__ == "__main__":

    dist = distribution(_package)

    data_path = dist.locate_file("format.json")

    print(type(data_path), data_path)

    for version in ["v1.0", "v2.0", "v2.1", "v2.2"]:

        try:
            format_data_path = format_by_version(version)
        except Exception as error:
            print(f"Problem finding format for {version=} {error}")
            continue

        print(f"{version=} -> {format_data_path}")
