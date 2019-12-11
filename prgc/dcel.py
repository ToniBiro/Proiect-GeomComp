from . import Vector2D


class Vertex:
    """
    Vertex of the polygon.

    Attributes
    ----------
    point: Vector2D
        coordinates of this vertex

    edge: Edge
        pointer to a half-edge leaving from this vertex
    """

    def __init__(self, point):
        self.point = point
        self.edge = None


class Edge:
    """
    Half-edge of the polygon.

    Attributes
    ----------
    target: Vertex
        the destination vertex of this edge

    face: Face
        pointer to the face bounded by this edge

    twin: Edge
        twin half-edge

    next: Edge
        following half-edge on this face

    prev: Edge
        preceeding half-edge on this face
    """

    def __init__(self, target):
        self.target = target
        self.face = None
        self.twin = None
        self.next = None
        self.prev = None

    def link(self, node):
        self.next = node
        node.prev = self


class Face:
    def __init__(self, edge):
        self.edge = edge


class DCEL:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.faces = []

    def create_vertex(self, point):
        vertex = Vertex(point)
        self.vertices.append(vertex)

        return vertex

    def create_edge(self, start, end):
        assert start in self.vertices
        assert end in self.vertices

        edge = Edge(end)
        self.edges.append(edge)

        return edge

    def create_face(self, edge):
        assert edge in self.edges

        face = Face(edge)
        self.faces.append(face)

        return face

    def make_twin(self, e1, e2):
        assert e1 in self.edges
        assert e2 in self.edges

        e1.twin = e2
        e2.twin = e1
