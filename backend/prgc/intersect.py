"Intersection functions and support structures"
from .primitive import Vector2D, right_turn


class Segment:
    "Line segment, identified by its two endpoints"

    def __init__(self, fp, sp):
        self.fp = fp
        self.sp = sp

    def slope(self):
        if self.sp.x - self.fp.x == 0:
            return None
        return float((self.sp.y - self.fp.y) / (self.sp.x - self.fp.x))

    def to_line(self):
        slope = self.slope()
        if slope == None:
            return Line(1, 0, -self.fp.x)
        return Line(slope, -1, self.fp.y - slope * self.fp.x)

    def __repr__(self):
        return f'Segment({self.fp} -> {self.sp})'

    def maximum(self):
        if self.fp > self.sp:
            return self.fp
        else:
            return self.sp

    def minimum(self):
        if self.fp < self.sp:
            return self.fp
        else:
            return self.sp


class Line:
    "Straight line in the plane"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def get_determinant(line1, line2):
    "Computes the 2D determinant from the coefficients of two lines"
    return line1.a * line2.b - line2.a * line1.b


def intersect_segments(seg1, seg2):
    """Computes the intersection of two line segments.

    Parameters
    ----------
    seg1: Segment
        The first segment
    seg2: Segment
        The second segment

    Returns
    -------
    `None` if they don't intersect or the point of intersection if they do
    """
    line1, line2 = seg1.to_line(), seg2.to_line()
    det = get_determinant(line1, line2)

    if det != 0:
        # calculam punctele de intersectie a celor doua drepte
        x = ((-line1.c) * line2.b - ((-line2.c) * line1.b)) / det
        y = (line1.a * (-line2.c) - (line2.a * (-line1.c))) / det

        # cazul in care avem intersectie de segmente
        if max(seg1.fp.x, seg1.sp.x) >= x >= min(seg1.fp.x, seg1.sp.x) and max(seg2.fp.x, seg2.sp.x) >= x >= min(seg2.fp.x, seg2.sp.x):
            if max(seg1.fp.y, seg1.sp.y) >= y >= min(seg1.fp.y, seg1.sp.y) and max(seg2.fp.y, seg2.sp.y) >= y >= min(seg2.fp.y, seg2.sp.y):
                return Vector2D(x, y)

    if det == 0:
        print(seg1, seg2, seg1.slope(), seg2.slope())
        if seg1.slope() == seg2.slope():
            if seg1.fp.x * line2.a + seg1.fp.y * line2.b == -line2.c:
                max_ = min(seg1.maximum(), seg2.maximum())
                min_ = max(seg1.minimum(), seg2.minimum())
                print(max_, min_)
                if max_ > min_:
                    return [min_, max_]
    return None


def intersect_polygons(dcel, poly_a, poly_b):
    "Computes the intersection of two polygons stored in a common DCEL"

    figures_isect = []

    ok = True
    while ok:
        ok = False
        for current_edge in filter(lambda e: e.face == poly_a, dcel.edges):
            for other_edge in filter(lambda e: e.face == poly_b, dcel.edges):
                # Skip self-intersections at polygon vertices
                if ((current_edge.target == other_edge.start) or
                    (current_edge.target == other_edge.target) or
                    (current_edge.start == other_edge.start) or
                        (current_edge.start == other_edge.target)):
                    continue

                seg1 = Segment(current_edge.start, current_edge.target)
                seg2 = Segment(other_edge.start, other_edge.target)
                result = intersect_segments(seg1, seg2)

                if result:
                    if isinstance(result, Vector2D):
                        if ((result == current_edge.start) or (result == current_edge.target)
                                or (result == other_edge.start) or (result == other_edge.target)):
                            figures_isect.append([result.to_tuple()])
                            continue

                        ipoint = dcel.create_vertex(result)

                        edge1 = current_edge
                        edge2 = other_edge

                        dcel.split(edge1, ipoint)
                        dcel.split(edge2, ipoint)

                        a = edge1
                        b = edge1.next
                        c = edge2
                        d = edge2.next

                        a_twin = a.twin
                        b_twin = b.twin
                        c_twin = c.twin
                        d_twin = d.twin

                        if right_turn(a.start, a.target, c_twin.target):
                            a.link(d)
                            d_twin.link(b)
                            b_twin.link(c_twin)
                            c.link(a_twin)

                            a.intersection = True
                            b.intersection = False
                            c.intersection = False
                            d.intersection = True
                        else:
                            a.link(c_twin)
                            c.link(b)
                            b_twin.link(d)
                            d_twin.link(a_twin)

                            a.intersection = False
                            b.intersection = True
                            c.intersection = True
                            d.intersection = False

                        ok = True

                        break
                    if isinstance(result, list):
                        a, b = result
                        print(result)
                        a.intersection = True
                        b.intersection = True

                        seg1.fp.intersection = True
                        seg1.sp.intersection = True
                        seg2.fp.intersection = True
                        seg2.sp.intersection = True

                        figures_isect.append(
                            [a.point.to_tuple(), b.point.to_tuple()])
                        print(figures_isect[-1])

                        ok = False

                        break

                    raise NotImplementedError

    loops = []
    visited = set()

    for edge in dcel.edges:
        if edge in visited:
            continue

        loop = []
        while edge not in visited:
            visited.add(edge)
            loop.append(edge)

            edge = edge.next

        for loop_edge in loop:
            if hasattr(loop_edge, 'intersection'):
                if loop_edge.intersection:
                    loops.append(loop)
                    break

    return loops
