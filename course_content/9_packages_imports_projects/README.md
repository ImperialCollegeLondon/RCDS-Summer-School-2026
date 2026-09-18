# Cylinder Report

A small Python project, used in the "Packages, Imports and Project Organisation"
session of the summer school. It reads a list of cylinders and their dimensions
from a file and reports the volume of each one.

The session notebook, `packages_imports_projects.ipynb`, sits at the
top level of this project so that its cells can import the code directly.

## Usage

From this directory:

```
python report_cylinders.py
```

## Layout

| Path | Contents |
| --- | --- |
| `packages_imports_projects.ipynb` | The session notebook |
| `circles.py` | The area and circumference of a circle |
| `cylinders.py` | The volume of a cylinder, built on `circles.py` |
| `dimensions.py` | Reading the dimensions file |
| `report_cylinders.py` | The script you run: ties the other three together |
| `data/` | The dimensions file |
| `tests/` | Tests for the geometry |
