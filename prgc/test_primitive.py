from prgc import Vector2D


def test_format_vector():
    v = Vector2D(5.3, -2.1)
    assert str(v) == f'(5.300, -2.100)'


def test_vector_add():
    v1 = Vector2D(-2, 4)
    v2 = Vector2D(3, 1)
    sum = v1 + v2
    assert sum == Vector2D(1, 5)


def test_vector_sub():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(5, -3)
    diff = v2 - v1
    assert diff == Vector2D(2, -7)
