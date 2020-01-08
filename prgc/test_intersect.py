from prgc import Segment, Vector2D, intersection

a = Vector2D(0, 0)
b = Vector2D(8, 8)
c = Vector2D(4, 2)
d = Vector2D(0, 8)

p = Vector2D(4, 3)

seg1 = Segment(a, b)
seg2 = Segment(c, d)
seg3 = Segment(a, d)
seg4 = Segment(b, p)


def test_intersect_two_segments():
    assert intersection(seg1, seg2) == Vector2D(3.2, 3.2)
