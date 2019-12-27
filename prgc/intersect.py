from . import Vector2D


class Segment:
    def __init__(self, fp, sp):
        self.fp = fp
        self.sp = sp

    def slope(self):
        if self.sp.x - self.fp.x == 0:
            return 0
        return float((self.sp.y - self.fp.y) / (self.sp.x - self.fp.x))

    def to_line(self):
        slope = self.slope()
        return Line(slope, -1, self.fp.y - slope * self.fp.x)

    def __repr__(self):
        return f'Segment({self.fp} -> {self.sp})'


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def get_determinant(line1, line2):
    return line1.a * line2.b - line2.a * line1.b


def intersection(seg1, seg2):
    """
    :param seg1: the first segment
    :param seg2: the second segment
    :return: None if they don't intersect and the point of intersection if they do
    """
    line1, line2 = seg1.to_line(), seg2.to_line()
    det = get_determinant(line1, line2)

    if det != 0:
        # calculam punctele de intersectie a celor doua drepte
        x = ((-line1.c) * line2.b - ((-line2.c) * line1.b)) / det
        y = (line1.a * (-line2.c) - (line2.a * (-line1.c))) / det

        if max(seg1.fp.x, seg1.sp.x) >= x >= min(seg1.fp.x, seg1.sp.x) and max(seg2.fp.x, seg2.sp.x) >= x >= min(seg2.fp.x, seg2.sp.x):  # cazul in care avem intersectie de segmente
            if max(seg1.fp.y, seg1.sp.y) >= y >= min(seg1.fp.y, seg1.sp.y) and max(seg2.fp.y, seg2.sp.y) >= y >= min(seg2.fp.y, seg2.sp.y):
                return Vector2D(x, y)
    return None


def intersect_segments(segments):
    for i, segment1 in enumerate(segments):
        for j in range(i+1, len(segments)):
            rez = intersection(segment1, segments[j])
            if rez: # it returns the coordinates of the intersections
                yield rez, segment1, segments[j]
