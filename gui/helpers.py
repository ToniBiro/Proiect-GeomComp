from prgc import Vector2D, DCEL, intersect_polygons


def read_polygon(dcel, file):
    num_points = int(next(file))
    points = [Vector2D.read(file) for _ in range(num_points)]
    return dcel.create_face_from_points(points)


def load_from_file(path):
    dcel = DCEL()
    with open(path) as file:
        polygon1 = read_polygon(dcel, file)
        polygon2 = read_polygon(dcel, file)
    return dcel, polygon1, polygon2


def face_to_point_list(face):
    points = []
    for edge in face:
        points.append(edge.start.point.to_tuple())
    return points
