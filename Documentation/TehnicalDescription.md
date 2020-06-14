# Documentation: Tehnical Description

## Contributors
- [Majeri Gabriel Constantin](https://github.com/GabrielMajeri) (232)
- [Biro-Balan Antonia](https://github.com/ToniBiro) (232)
- [Surcea Mihai-Daniel](https://github.com/Treefold) (232)


## List of Features for Backend
All classes ([Vector2D](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L4), [Segment](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/intersect.py#L4), [Line](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/intersect.py#L38), [Vertex](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L6), [Edge](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L47), [Face](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L96), [DCEL](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/dcel.py#L112)) are used to represent the structure of a polygon which is needed in all backend features (get_polygon_info, compute_intersection).

- [get_polygon_info](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/app.py#L88): given 1 polygon as a polygonal chain as parameter, it shall return its [area](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L74), [perimeter](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L93) and [type](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/prgc/primitive.py#L119) (convex or concave)
- [compute_intersection](https://github.com/ToniBiro/Proiect-GeomComp/blob/45cf8b0ac8d0c27ce7710e266fcc4e2ed4da49e9/backend/app.py#L19): given 2 polygons as polygonal chains as parameters, transform them in doubly connected edge list and perform the intersection; the returned value shall contain the fist polygon without the intersection, the second polygon without the intersection and the intersection reprezented as multiple polygonal chains

## Diagram of Classes for Backend

![image](https://github.com/ToniBiro/Proiect-GeomComp/blob/master/Documentation/diagram_classes_backend.png)
