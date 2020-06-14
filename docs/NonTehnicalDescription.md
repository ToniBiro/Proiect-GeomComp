# Documentation

## Contributors
- [Majeri Gabriel Constantin](https://github.com/GabrielMajeri) (232)
- [Biro-Balan Antonia](https://github.com/ToniBiro) (232)
- [Surcea Mihai-Daniel](https://github.com/Treefold) (232)

## User Stories
```
As a user I want to add a polygon so that I intersect more polygons.
As a user I want to change the color of any polygon so that I can distinguish between them more easily.
As a user I want to add a vertex to the current polygon so that I can make my current polygon more complex.
As a user I want to change my current polygon so that I can edit another polygon.
As a user I want to move a vertex of any polygon by drag and drop to another position so that I change any polygon without changing the current polygon.
As a user I want to change a vertex of the current polygon by changing its coordinates so that I can move a vertex to a specific position.
As a user I want to move the polygon as a whole figure so that I don’t have to move each vertex at a time.
As a user I want to make visible or hide any polygon defined by me so that I can choose which one to use for the intersection.
As a user I want to press the get intersection button so that I can see the intersection between the polygons.
As a user I want to change the color of the intersections so that I can see it more clearly.
As a user I want to see the perimeter and area of all polygons changed when one polygon is changed so that I don’t have to calculate it manually.
As a user I want to delete a vertex so that I make my poligon simpler.
As a user I want to delete the whole poligon so that I don’t have to delete it one vertex at a time.
As a user I want to be able to name my polygons so that I find them more easily.
```

## Features:
- #### Server (backend):
  - get_polygon_info
  - compute_intersection
- #### Interface (frontend):
  - addPolygon
  - setCurrentPolygon
  - addVertex
  - setVertexPosition

## Behavior Description 
- #### Server (backend):
  - get_polygon_info: given 1 polynom, it shall return the area, perimeter and the type (convex, concave) of that polynom
  - compute_intersection: given 2 polynoms, it shall return 3 list containing the components of the first polynom except the intersection, the second polynom except the intersection and a polynom of the intersection
- #### Interface (frontend):
  - addPolygon: shall add an empty polygon (no vertices)
  - setCurrentPolygon: shall change the current modified polygon
  - addVertex: shall add a vertex in the selected polygon 
  - setVertexPosition: shall change a vertex position for a polygon

## Visual Aspect Description
- #### Interface (frontend):
  - addPolygon: shall create a new empty poligon and 2 buttons: "Make current" (polygon) and "Add New" (vertex)
  - setCurrentPolygon: shall disable the fuction for the button "Make current" for the new current polygon and shall enable the "Make Current" button for the previous current polygon
  - addVertex: shall create a vertex where you click in the drawing zone and the vertex shall be displayed in the polygon vertex list with the coordinates of the click; if there are less than 3 vertice in this polynom then after adding the new vertex, all vertices shall be connected, else (there are 3 or more vertices) the last connection shall be removed and the new vertex shall connect to the previous last vertex (becoming the new last vertex) and the first created vertex
  - setVertexPosition: by clicking and dragging a vertex, it shall move to the location where it was released; also, the position of the vertex shall be updated in the polygon vertex list
