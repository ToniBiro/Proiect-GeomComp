/**
 * Action types
 */

export const ADD_POLYGON = "ADD_POLYGON";
export const SET_VERTEX_POSITION = "SET_VERTEX_POSITION";

/**
 * Action creators
 */

export function addPolygon() {
  return { type: ADD_POLYGON };
}

export function setVertexPosition(polygonIndex, vertexIndex, x, y) {
  return {
    type: SET_VERTEX_POSITION,
    polygonIndex,
    vertexIndex,
    newPosition: { x, y },
  };
}
