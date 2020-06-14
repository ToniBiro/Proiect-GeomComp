# Documentation: Tehnical Description

## Contributors
- [Majeri Gabriel Constantin](https://github.com/GabrielMajeri) (232)
- [Biro-Balan Antonia](https://github.com/ToniBiro) (232)
- [Surcea Mihai-Daniel](https://github.com/Treefold) (232)

## List of Classes for Backend:
- [Vector2D](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L4): is a vector with 2 components (a point in a 2D plan)
  - x (property): reprezents the coordinates of the x axis (real number)
  - y (property): reprezents the coordinates of the y axis (real number)
  - [to_tuple](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L24): shall transform the current vector to a tuple
  - [read](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L60): (static) shall return the next vector2D read from a specified file (as parameter)
- [Line](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/intersect.py#L38): this class resembles a line by its equation coefficients; the equation of line is written as following a*x+b*y+c = 0
  - a (property): repezents the x coefficient of the line equation (real number)
  - b (property): repezents the y coefficient of the line equation (real number)
  - c (property): repezents the free coefficient of the line equation (real number)
- [Segment](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/intersect.py#L4): is a line delimited by 2 Vector2D points
  - fp (property): repezents the first point (Vector2D) of the segment
  - sp (property): repezents the second point (Vector2D) of the segment
  - [slope](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/intersect.py#L11): shall return the slope of the current line
  - [to_line](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/intersect.py#L16): shall return a Line object on with both Vector2D point belong
  - [maximum](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/intersect.py#L25): shall return the Vector2D with the greatest x component and if they are equal then the greatest y component (the 2 vectors can’t be the same because that’s an incorrect line)
  - [minimum](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/intersect.py#L31): shall return the Vector2D with the lowest x component and if they are equal then the lowest y component (the 2 vectors can’t be the same because that’s an incorrect line)
- [Vertex](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L6): represents a point(Vector2D) of the polygon and it knows the half-edge that start from this point:
  - point (property): repezents the a point (Vector2D) of the polynom
  - edge (property): repezents the half-edge (Edge) of the polynom that start with the given point (property)
  - [x](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L39): shall return the x component of this vertex
  - [y](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L43): shall return the y component of this vertex
- [Edge](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L47): represents a helf-edge that know only the endpoind and can figure out the starting poing from its twin (which is the endpoint for its twin), it also knows the previous and the next edge of the current face
  - target (property): repezents the destination Vertex of this edge
  - face (property): repezents a pointer to the Face bounded by this edge
  - twin (property): repezents a pointer to the twin half-edge (Edge)
  - next (property): repezents a pointer to the following half-edge (Edge) on this face
  - prev (property): repezents a pointer to the preceeding half-edge (Edge) on this face
  - [link](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L79): shall connect the currnet Edge (self) with its next Edge (given as a parameter)
  - [start](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L87): shall return the starting point which is the endpoint of its twin Edge
  - [to_segment](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L90): shall return a line of the stating and ending points of the current Edge (self)
- [Face](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L96): reprezents one of the faces of a polygon
  - edge (property): reprezents a pointer to one of the half-edges (Edge) that belongs to the current Face (self)
- [DCEL](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L112): reprezents a doubly connected edge list
  - vertices (property): reprezents an array of Vertix objects that belong to the DCEL 
  - edges (property): reprezents an array of Edge objects that belong to the DCEL 
  - faces (property): reprezents an array of Face objects that belong to the DCEL 
  - [create_vertex](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L118): shall add a new given vertex, initially not connected to anything
  - [create_edge](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L125): shall add a new edge, connecting the two given vertices
  - [create_face](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L138): shall add a new face, the one to the left of the given edge
  - [make_twin](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L147): shall make the 2 given Edges the twin of the other one
  - [split](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L154): shall add a new vertex on a Edge by destroing the current Edge and shall connect the previous connected vertices to the new vertex
  - [add_intersection](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L180): shall be implemented in the future
  - [create_face_from_points](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L186): shall create a face from an array of points (Vector2D)

## Diagram of Classes for Backend

![image](https://github.com/ToniBiro/Proiect-GeomComp/blob/master/Documentation/diagram_classes_backend.png)


## List of Features for Backend:
*All classes are used to represent the structure of a polygon which is needed in all backend features

- [get_polygon_info](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/app.py#L88): given 1 polygon as a polygonal chain as parameter, it shall return its [area](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L74), [perimeter](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L93) and [type](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L119) (convex or concave)
- [compute_intersection](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/app.py#L19): given 2 polygons as polygonal chains as parameters, transform them in doubly connected edge list and perform the intersection; the returned value shall contain the fist polygon without the intersection, the second polygon without the intersection and the intersection reprezented as multiple polygonal chains
