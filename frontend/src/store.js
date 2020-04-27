import { createStore } from "redux";

const ADD_POLYGON = "ADD_POLYGON";
const SET_VERTEX_POSITION = "SET_VERTEX_POSITION";

export function addPolygon() {
  return {
    type: ADD_POLYGON,
  };
}

export function setVertexPosition(polygonIndex, vertexIndex, x, y) {
  return {
    type: SET_VERTEX_POSITION,
    polygonIndex,
    vertexIndex,
    newPosition: { x, y },
  };
}

function reducer(state, action) {
  switch (action.type) {
    case ADD_POLYGON:
      return [
        ...state,
        {
          vertices: [],
        },
      ];
    case SET_VERTEX_POSITION:
      const polygon = state[action.polygonIndex];

      const newVertices = polygon.vertices.slice();
      newVertices.splice(action.vertexIndex, 1, action.newPosition);

      const newPolygon = {
        vertices: newVertices,
      };

      const newState = state.slice();
      newState.splice(action.polygonIndex, 1, newPolygon);

      return newState;
    default:
      return [
        {
          vertices: [
            {
              x: 23,
              y: 20,
            },
            {
              x: 23,
              y: 160,
            },
            {
              x: 70,
              y: 93,
            },
            {
              x: 150,
              y: 109,
            },
          ],
        },
      ];
  }
}

const store = createStore(reducer);

export default store;
