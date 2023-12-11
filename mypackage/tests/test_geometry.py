import numpy as np

from ..geometry.geometry import Line, Point, distance


def test_distance():
    p1 = Point(1, 3)
    p2 = Point(2, 4)
    assert distance(p1, p2) == np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def test_point():
    point = Point(3, 2)
    assert point.x == 3
    assert point.y == 2


def test_line():
    p1 = Point(1, 3)
    p2 = Point(3, 5)
    line = Line(p1, p2)
    assert line.p1 == p1
    assert line.p2 == p2
    assert line.length() == distance(p1, p2)
