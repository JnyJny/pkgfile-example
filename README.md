# pkgfile - An Example of How to Retreive Data Files Embedded in Packages

There a couple of different strategies that we can employ to locate data
files that have been included in a python package. The most common strategy
is use the `__file__` variable in a loader-type function:

```python

from pathlib import Path

def path_for_file(name: str) -> Path:
    """Return the path for a file."""
    parent = Path(__file__).resolve().parent
	
    target = parent / name
	
    if not target.exists():
        raise FileNotFoundError(target)
		
    return target
```

This method is okay but is kind of fragile and the more code we write,
the more opportunities to introduce bugs.

An easier way to find files embedded in packages is using
`distribution` from the standard library `importlib.metadata`.

```python

from importlib.metadata import distribution

dist = distribution("my-package-name")

path = dist.locate_file("foo.data")
```

In this example, we remove the path construction which could change
over time (what if we embed our files more deeply within a
sub-package?) and the only things we need to know ahead of time are:

1. What is the name of the package
2. What is the name of the file we are looking for


