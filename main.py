from prgc import Vector2D

class Segment:
    def __init__(self, fp, sp):
        self.fp = fp
        self.sp = sp

    def slope(self):
        if self.sp.x - self.fp.x == 0:
            return 0
        return float((self.sp.y - self.fp.y) / (self.sp.x - self.fp.x))


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def get_determinant(line1, line2):
    return line1.a * line2.b - line2.a * line1.b


def data_processing(seg1, seg2):
    line1 = Line(seg1.slope(), -1, seg1.fp.y - seg1.slope()*seg1.fp.x)
    line2 = Line(seg2.slope(), -1, seg2.fp.y - seg2.slope()*seg2.fp.x)
    return line1, line2


def intersection(seg1, seg2):
    """
    :param seg1: the first segment
    :param seg2: the second segment
    :return: None if they don't intersect and the x, y if they do
    """
    line1, line2 = data_processing(seg1, seg2)
    det = get_determinant(line1, line2)

    if det != 0:
        x = ((-line1.c) * line2.b - ((-line2.c) * line1.b)) / det  # calculam punctele de intersectie a celor doua drepte
        y = (line1.a * (-line2.c) - (line2.a * (-line1.c))) / det

        if max(seg1.fp.x, seg1.sp.x) >= x >= min(seg1.fp.x, seg1.sp.x) and max(seg2.fp.x, seg2.sp.x) >= x >= min(seg2.fp.x, seg2.sp.x):  # cazul in care avem intersectie de segmente
            if max(seg1.fp.y, seg1.sp.y) >= y >= min(seg1.fp.y, seg1.sp.y) and max(seg2.fp.y, seg2.sp.y) >= y >= min(seg2.fp.y, seg2.sp.y):
                return x, y
    return None


def intersections(segments):
    seg_inter = []
    for i, segment1 in enumerate(segments):
        for j in range(i+1, len(segemnts)):
            rez = intersection(segment1, segments[j])
            if rez:
                seg_inter.append(rez) # it returns the coordinates of the intersections

    return seg_inter

# punct_a = Vector2D(0, 0)
# punct_b = Vector2D(8, 8)
#
# punct_c = Vector2D(4, 2)
# pp = Vector2D(4, 3)
# punct_d = Vector2D(0, 8)
#
# seg1 = Segment(punct_a, punct_b)
# seg2 = Segment(punct_c, punct_d)
# seg3 = Segment(punct_a, punct_d)
# seg4 = Segment(punct_b, pp)
#
# print(intersection(seg1, seg2))
#
# segemnts = [seg1, seg2, seg3, seg4]


# results = intersections(segemnts)
#
# print(f"results = {results}")