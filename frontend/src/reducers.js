import { combineReducers } from "redux";

import {
  ADD_POLYGON,
  SET_VERTEX_POSITION,
  SET_CURRENT_POLYGON,
} from "./actions";

const currentPolygonReducer = (state = 0, action) => {
  switch (action.type) {
    case SET_CURRENT_POLYGON:
      return action.polygonIndex;
    default:
      return state;
  }
};

const initialPolygonList = [
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

const polygonListReducer = (state = initialPolygonList, action) => {
  switch (action.type) {
    case ADD_POLYGON:
      return [
        ...state,
        {
          vertices: [],
        },
      ];
    default:
      return state.map((polygon) => polygonReducer(polygon, action));
  }
};

function polygonReducer(state, action) {
  switch (action.type) {
    case SET_VERTEX_POSITION:
      return {
        ...state,
        vertices: state.vertices.map((vertex, index) =>
          action.vertexIndex === index ? action.newPosition : vertex
        ),
      };
    default:
      return state;
  }
}

const rootReducer = combineReducers({
  currentPolygon: currentPolygonReducer,
  polygons: polygonListReducer,
});

export default rootReducer;
