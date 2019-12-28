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
        return f'({self.x}, {self.y})'

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
