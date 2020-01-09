import argparse

from prgc import DCEL, Vector2D, Segment, draw, intersection, right_turn

parser = argparse.ArgumentParser()
parser.add_argument("path", help="input file path")
args = parser.parse_args()

input_path = args.path


dcel = DCEL()

with open(input_path) as fin:
    poly_a = dcel.read_polygon_from_file(fin)
    poly_b = dcel.read_polygon_from_file(fin)


def face_to_segments(face):
    return [edge.to_segment() for edge in face]


def edges_to_figure(edges):
    figure = []

    for edge in edges:
        figure.append((edge.start.x, edge.start.y))

    return figure


figure_a = edges_to_figure(iter(poly_a))
figure_b = edges_to_figure(iter(poly_b))
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
            result = intersection(seg1, seg2)

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
                elif isinstance(result, list):
                    a, b = result
                    print(result)
                    a.intersection = True
                    b.intersection = True

                    seg1.fp.intersection = True
                    seg1.sp.intersection = True
                    seg2.fp.intersection = True
                    seg2.sp.intersection = True

                    figures_isect.append([a.point.to_tuple(), b.point.to_tuple()])
                    print(figures_isect[-1])

                    ok = False

                    break
                else:
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

    for edge in loop:
        if hasattr(edge, 'intersection'):
            if edge.intersection:
                loops.append(loop)
                break

for loop in loops:
    figure = edges_to_figure(loop)
    figures_isect.append(figure)

draw(figure_a, figure_b, figures_isect)
