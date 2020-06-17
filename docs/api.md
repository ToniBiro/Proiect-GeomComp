# Application Programming Interface

## Server (back end)

All calls are made using JSON.

- `get_polygon_info`: given 1 polygon, it shall return the area, perimeter and
  the type (convex, concave) of that polygon
- `compute_intersection`: given 2 polygons, it shall return a list
  containing the polygon(s) forming the intersection

## Client app (front end):

The following are Redux actions:

- `ADD_POLYGON`: shall add an empty polygon (no vertices)
- `SET_CURRENT_POLYGON`: shall disable the button "Make current" for the new current polygon and shall enable the "Make Current" button for the previous current polygon
- `ADD_VERTEX`: shall create a vertex where you click in the drawing zone and the vertex shall be displayed in the polygon vertex list with the coordinates of the click; if there are less than 3 vertice in this polygon then after adding the new vertex, all vertices shall be connected, else (there are 3 or more vertices) the last connection shall be removed and the new vertex shall connect to the previous last vertex (becoming the new last vertex) and the first created vertex
- `SET_VERTEX_POSITION`: by clicking and dragging a vertex, it shall move to the location where it was released; also, the position of the vertex shall be updated in the polygon vertex list
