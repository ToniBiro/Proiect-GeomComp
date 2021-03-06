/**
 * Action types
 */

export const ADD_POLYGON = "ADD_POLYGON";
export const DELETE_POLYGON = "DELETE_POLYGON";
export const SET_CURRENT_POLYGON = "SET_CURRENT_POLYGON";
export const ADD_VERTEX = "ADD_VERTEX";
export const SET_VERTEX_POSITION = "SET_VERTEX_POSITION";

/**
 * Action creators
 */

export function addPolygon(vertices = []) {
  return { type: ADD_POLYGON, vertices };
}

export function deletePolygon(polygonIndex) {
  return { type: DELETE_POLYGON, polygonIndex };
}

export function setCurrentPolygon(polygonIndex) {
  return { type: SET_CURRENT_POLYGON, polygonIndex };
}

export function addVertex(polygonIndex, position) {
  return { type: ADD_VERTEX, polygonIndex, position };
}

export function setVertexPosition(polygonIndex, vertexIndex, x, y) {
  return {
    type: SET_VERTEX_POSITION,
    polygonIndex,
    vertexIndex,
    newPosition: { x, y },
  };
}
