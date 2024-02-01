"""
"""


from importlib.metadata import distribution


if __name__ == "__main__":

    dist = distribution("pkgfile")

    data_path = dist.locate_file("format.json")

    print(type(data_path), data_path)
