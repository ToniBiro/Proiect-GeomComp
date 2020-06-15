"""Doubly connected edge list representation for polygons."""

from io import StringIO
from .intersect import Segment


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

    def __repr__(self):
        return f'Vertex{self.point}'

    def __lt__(self, other):
        return self.point < other.point

    def __le__(self, other):
        return self.point <= other.point

    def __gt__(self, other):
        return self.point > other.point

    def __ge__(self, other):
        return self.point >= other.point

    @property
    def x(self):
        return self.point.x

    @property
    def y(self):
        return self.point.y


class Edge:
    """
    Half-edge of the polygon.

    Attributes
    ----------
    start: Vertex
        the source vertex of this edge

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

    def link(self, edge):
        self.next = edge
        edge.prev = self

    def __repr__(self):
        return f'Edge({self.prev.target} -> {self.target})'

    @property
    def start(self):
        return self.twin.target

    def to_segment(self):
        segment = Segment(self.start, self.target)
        segment.edge = self
        return segment


class Face:
    """Closed loop of edges, defining a face of a 2D shape"""

    def __init__(self, edge):
        self.edge = edge
        for edge in self:
            edge.face = self

    def __iter__(self):
        start = self.edge
        yield start

        current = start.next
        while current != start:
            yield current
            current = current.next


class DCEL:
    """Store of vertices, edges and faces, representing one or more polygons.

    For each polygon, we store its internal face, defined by a counter-clockwise
    wound traversal of its vertices, and its external face,
    which is clockwise wound.
    """

    def __init__(self):
        self.vertices = []
        self.edges = []
        self.faces = []

    def create_vertex(self, point):
        "Adds a new vertex, initially not connected to anything."
        vertex = Vertex(point)
        self.vertices.append(vertex)

        return vertex

    def create_edge(self, start, end):
        "Adds a new edge, connecting the two given vertices."
        assert start in self.vertices
        assert end in self.vertices

        edge = Edge(end)
        self.edges.append(edge)

        start.edge = edge
        end.edge = edge

        return edge

    def create_face(self, edge):
        "Adds a new face, the one to the left of the edge."
        assert edge in self.edges

        face = Face(edge)
        self.faces.append(face)

        return face

    def make_twin(self, e1, e2):
        "Makes two edges be twins to one another"
        assert e1 in self.edges
        assert e2 in self.edges

        e1.twin = e2
        e2.twin = e1

    def split(self, edge, vertex):
        """Split the given edge (and its twin) into new edges,
        at a given vertex.

        The vertex needn't be on the edge.
        """
        assert vertex in self.vertices
        assert edge in self.edges

        a = edge.start
        b = edge.target

        twin = edge.twin

        new_direct_edge = self.create_edge(vertex, b)
        new_direct_edge.link(edge.next)
        new_direct_edge.face = edge.face

        new_reverse_edge = self.create_edge(vertex, a)
        new_reverse_edge.link(twin.next)
        new_reverse_edge.face = edge.twin.face

        edge.link(new_direct_edge)
        twin.link(new_reverse_edge)

        edge.target = vertex
        twin.target = vertex

        self.make_twin(edge, new_reverse_edge)
        self.make_twin(new_direct_edge, twin)

    def create_face_from_points(self, points):
        """Creates a new face from a set of points.

        The winding is done counter-clockwise.
        """
        vertices = [
            self.create_vertex(point)
            for point in points
        ]
        num_vertices = len(vertices)

        inner_edges = []
        outer_edges = []

        for i in range(num_vertices - 1):
            inner = self.create_edge(vertices[i], vertices[i + 1])
            outer = self.create_edge(vertices[i + 1], vertices[i])

            self.make_twin(inner, outer)

            inner_edges.append(inner)
            outer_edges.append(outer)

        inner = self.create_edge(vertices[num_vertices - 1], vertices[0])
        outer = self.create_edge(vertices[0], vertices[num_vertices - 1])

        self.make_twin(inner, outer)

        inner_edges.append(inner)
        outer_edges.append(outer)

        for i in range(num_vertices - 1):
            inner_edges[i].link(inner_edges[i + 1])
        inner_edges[-1].link(inner_edges[0])

        for i in range(num_vertices - 1):
            outer_edges[i + 1].link(outer_edges[i])
        outer_edges[0].link(outer_edges[-1])

        inner_face = self.create_face(inner_edges[0])

        return inner_face

    def __repr__(self):
        with StringIO() as out:
            print('DCEL(', file=out)

            print(f'  Vertices: {self.vertices}', file=out)
            print(f'  Edges: {self.edges}', file=out)
            print(f'  Faces: {self.faces}', file=out)

            print(')', file=out)

            return out.getvalue()
