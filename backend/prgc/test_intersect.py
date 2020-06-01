from .primitive import Vector2D
from .intersect import Segment
from .dcel import DCEL
from .intersect import intersect_segments, intersect_polygons


def assert_edge_from_to(edge, start, target):
    assert edge.start.point == start
    assert edge.target.point == target


def test_intersect_two_segments():
    a = Vector2D(0, 0)
    b = Vector2D(8, 8)
    c = Vector2D(4, 2)
    d = Vector2D(0, 8)

    p = Vector2D(4, 3)

    seg1 = Segment(a, b)
    seg2 = Segment(c, d)
    seg3 = Segment(a, d)
    seg4 = Segment(b, p)

    assert intersect_segments(seg1, seg2) == Vector2D(3.2, 3.2)
    assert intersect_segments(seg1, seg3) == Vector2D(0, 0)
    assert intersect_segments(seg3, seg4) is None


def test_intersect_two_rectangles():
    dcel = DCEL()

    rect1 = dcel.create_face_from_points([
        Vector2D(0, 0),
        Vector2D(1, 0),
        Vector2D(1, 1),
        Vector2D(0, 1),
    ])
    rect2 = dcel.create_face_from_points([
        Vector2D(0.5, -0.25),
        Vector2D(1.25, -0.25),
        Vector2D(1.25, 1.5),
        Vector2D(0.5, 1.5)
    ])

    isect = intersect_polygons(dcel, rect1, rect2)
    assert len(isect) == 1, "Result of intersection should be a single polygon"

    # Extract the result
    isect = isect[0]
    assert len(isect) == 4, "Result of intersection should be quadrilateral"

    assert_edge_from_to(isect[0], Vector2D(1, 0), Vector2D(1, 1))
    assert_edge_from_to(isect[1], Vector2D(1, 1), Vector2D(0.5, 1))
    assert_edge_from_to(isect[2], Vector2D(0.5, 1), Vector2D(0.5, 0))
    assert_edge_from_to(isect[3], Vector2D(0.5, 0), Vector2D(1, 0))