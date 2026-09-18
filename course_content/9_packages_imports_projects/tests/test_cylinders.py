"""Tests for the cylinders module."""

from circles import circle_area
from cylinders import cylinder_volume


def test_a_cylinder_of_height_one_is_just_its_circle():
    assert cylinder_volume(2, 1) == circle_area(2)


def test_volume_doubles_when_height_doubles():
    assert cylinder_volume(1, 2) == 2 * cylinder_volume(1, 1)


def test_no_height_means_no_volume():
    assert cylinder_volume(3, 0) == 0


def test_no_radius_means_no_volume():
    assert cylinder_volume(0, 5) == 0
