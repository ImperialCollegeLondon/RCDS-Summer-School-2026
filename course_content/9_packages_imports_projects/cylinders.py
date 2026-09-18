"""Functions for the geometry of cylinders."""

# This relies on circles.py being in the same directory as this file
from circles import circle_area


def cylinder_volume(radius, height):
    """Return the volume of a cylinder of the given radius and height."""
    return circle_area(radius) * height
