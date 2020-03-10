import pytest

from . import DCEL, Vector2D


def create_triangle_and_segment():
    dcel = DCEL()

    a = dcel.create_vertex(Vector2D(0.0, 0.0))
    b = dcel.create_vertex(Vector2D(0.0, 1.0))
    c = dcel.create_vertex(Vector2D(1.0, 0.0))
    d = dcel.create_vertex(Vector2D(2.0, 0.0))

    # Triangle interior
    ac = dcel.create_edge(a, c)
    cb = dcel.create_edge(c, b)
    ba = dcel.create_edge(b, a)

    ac.link(cb)
    cb.link(ba)
    ba.link(ac)

    # Add a face for the interior of the triangle
    triangle = dcel.create_face(ac)

    # Outside contour
    ab = dcel.create_edge(a, b)
    bc = dcel.create_edge(b, c)
    cd = dcel.create_edge(c, d)
    dc = dcel.create_edge(d, c)
    ca = dcel.create_edge(c, a)

    ab.link(bc)
    bc.link(cd)
    cd.link(dc)
    dc.link(ca)
    ca.link(ab)

    # Outside face
    dcel.create_face(ab)

    # Pair up the half-edges
    dcel.make_twin(ac, ca)
    dcel.make_twin(cb, bc)
    dcel.make_twin(ba, ab)
    dcel.make_twin(cd, dc)

    return dcel, triangle


def test_create_dcel():
    dcel, triangle = create_triangle_and_segment()

    # 4 points: A, B, C, D
    assert len(dcel.vertices) == 4
    # 3 inside edges and 5 outside edges
    assert len(dcel.edges) == 8
    # Triangle and outside face
    assert len(dcel.faces) == 2


@pytest.mark.skip(reason="only prints DCEL for manual inspection")
def test_print_dcel():
    dcel, triangle = create_triangle_and_segment()

    for edge in triangle:
        print(edge)

    print()

    for edge in dcel.faces[-1]:
        print(edge)

    assert False


def test_add_intersection():
    dcel, triangle = create_triangle_and_segment()

    a = dcel.create_vertex(Vector2D(0.25, 0.25))
    b = dcel.create_vertex(Vector2D(2.0, 2.0))

    ab = dcel.create_edge(a, b)
    ba = dcel.create_edge(b, a)

    ab.link(ba)
    ba.link(ab)

    dcel.make_twin(ab, ba)

    assert len(dcel.vertices) == 6
