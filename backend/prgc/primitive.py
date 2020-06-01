import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x:.3f}, {self.y:.3f})'

    def to_tuple(self):
        return (self.x, self.y)

    def __lt__(self, other):
        if self.y < other.y:
            return True
        if self.y == other.y:
            if self.x < other.x:
                return True
        return False

    def __gt__(self, other):
        if self.y > other.y:
            return True
        if self.y == other.y:
            if self.x > other.x:
                return True
        return False

    def __le__(self, other):
        if self.y < other.y:
            return True
        if self.y == other.y:
            if self.x <= other.x:
                return True
        return False

    def __ge__(self, other):
        if self.y > other.y:
            return True
        if self.y == other.y:
            if self.x >= other.x:
                return True
        return False

    @staticmethod
    def read(file):
        line = next(file)
        x, y = map(float, line.split())
        return Vector2D(x, y)


Vector2D.ORIGIN = Vector2D(0, 0)


def right_turn(a, b, c):
    "Checks if the point c is to the right of the a-b line."
    return ((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)) < 0

def compute_area(polygon):
    """
    Computes the area of a polygon.
    Input: A list of points
    e.g. polygon = [(0, 0), (1, 0), (1, 1), (0, 1)]
    """
    area = 0.5 * abs(sum([polygon[i][0] * polygon[i+1][1] for i in range(0, len(polygon) - 1)]) + polygon[len(polygon)-1][0] * polygon[0][1]
                - sum([polygon[i+1][0] * polygon[i][1] for i in range(0, len(polygon) - 1)]) - polygon[0][0] * polygon[len(polygon)-1][1])
    
    return area

def calculate_distance(point_1, point_2):
    """
    Returns the euclidian distance between 2 points
    """
    return math.sqrt((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)

def compute_perimeter(polygon):
    """
    Computes and returns the perimeter of a given simple polygon.
    Input: a list of points
    e.g. polygon = [(0, 0), (1, 0), (1, 1), (0, 1)]
    """
    perimeter = 0
    for i in range(0, len(polygon)-1):
        perimeter += calculate_distance(polygon[i], polygon[i+1])
    perimeter += calculate_distance(polygon[0], polygon[-1])

    return perimeter

def cross_product(point_1, point_2, point_3):
    """
    Computes the cross product of 3 given points in 2D
    """
    a = point_2[0] - point_1[0]
    b = point_2[1] - point_1[1]
    c = point_3[0] - point_2[0]
    d = point_3[1] - point_2[1]

    return a * d - b * c


def define_polygon_type(polygon):
    """
    Returns either concav or convex.
    """
    check = cross_product(polygon[len(polygon)-2], polygon[len(polygon)-1], polygon[0]) <= 0
    convex = (check == (cross_product(polygon[len(polygon)-1], polygon[0], polygon[1]) <= 0))
    for i in range(0, len(polygon)-2):
        convex = check == (cross_product(polygon[i], polygon[i+1], polygon[i+2]) <= 0)

    if convex == True:
        return 'convex'
    else:
        return 'concave'