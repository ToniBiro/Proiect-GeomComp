from .primitive import Vector2D
from .dcel import DCEL


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