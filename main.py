from prgc import DCEL, Vector2D, draw, intersect_segments
from prgc.intersect import Segment, intersection

dcel = DCEL()

with open('input.txt') as fin:
    a = dcel.read_polygon_from_file(fin)
    b = dcel.read_polygon_from_file(fin)

def face_to_segments(face):
    return [edge.to_segment() for edge in face]

segments_a = face_to_segments(a)
segments_b = face_to_segments(b)

print(segments_a + segments_b)

for intersection, seg1, seg2 in intersect_segments(segments_a + segments_b):
    if isinstance(intersection, Vector2D):
        # Skip self-intersections
        # TODO: modify intersection code to avoid them
        if seg1.edge.face == seg2.edge.face:
            continue

        ipoint = dcel.create_vertex(intersection)
        print(ipoint)

        print(seg1.edge)
        dcel.split(seg1.edge, ipoint)
        print(seg1.edge, seg1.edge.next)
        dcel.split(seg2.edge, ipoint)
    else:
        raise NotImplementedError

print(dcel)

figures = []
for face in dcel.faces:
    for edge in face:
        figures.append([(edge.start.x, edge.start.y), (edge.target.x, edge.target.y)])
        if edge.face != face:
            print(edge)

draw([], [], figures, 'red', 'blue', 'yellow')
