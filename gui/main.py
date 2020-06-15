from copy import deepcopy
from plot import draw
from prgc import intersect_polygons
from helpers import *

# Load some sample polygons
dcel, polygon1, polygon2 = load_from_file("inputs/square_tri.txt")

p1_points = face_to_point_list(polygon1)
p2_points = face_to_point_list(polygon2)

# Intersect them
result = intersect_polygons(dcel, polygon1, polygon2)
result_points = [face_to_point_list(poly) for poly in result]

# Show the result
draw(p1_points, p2_points, result_points)
