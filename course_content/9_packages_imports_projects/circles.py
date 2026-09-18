"""Functions for the geometry of circles."""

import math


def circle_area(radius):
    """Return the area of a circle of the given radius."""
    return math.pi * radius ** 2


def circle_circumference(radius):
    """Return the circumference of a circle of the given radius."""
    return 2 * math.pi * radius
