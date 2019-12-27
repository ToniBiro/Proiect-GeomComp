from prgc import DCEL


dcel = DCEL()

with open('input.txt') as fin:
    a = dcel.read_polygon_from_file(fin)
    b = dcel.read_polygon_from_file(fin)

print(dcel)
