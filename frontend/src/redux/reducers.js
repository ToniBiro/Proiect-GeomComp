import { combineReducers } from "redux";

import {
  ADD_POLYGON,
  SET_CURRENT_POLYGON,
  ADD_VERTEX,
  SET_VERTEX_POSITION,
  DELETE_POLYGON,
} from "./actions";

const currentPolygonReducer = (state = 0, action) => {
  switch (action.type) {
    case DELETE_POLYGON:
      const index = action.polygonIndex;
      if (index <= state) {
        if (state > 0) {
          return state - 1;
        }
      }
      return state;
    case SET_CURRENT_POLYGON:
      return action.polygonIndex;
    default:
      return state;
  }
};

const initialPolygonList = [
  {
    color: "rgba(0, 210, 255, 0.4)",
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
        x: 73,
        y: 100,
      },
      {
        x: 150,
        y: 109,
      },
      {
        x: 120,
        y: 61.21,
      },
    ],
  },
  {
    color: "rgba(100, 230, 50, 0.4)",
    vertices: [
      {
        x: 122,
        y: 156.21,
      },
      {
        x: 214,
        y: 59.21,
      },
      {
        x: 87,
        y: 83.21,
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
          color: randomColor(),
          vertices: action.vertices,
        },
      ];
    case DELETE_POLYGON:
      const index = action.polygonIndex;
      return [...state.slice(0, index), ...state.slice(index + 1)];
    default:
      return state.map((polygon, index) =>
        polygonReducer(polygon, index, action)
      );
  }
};

function polygonReducer(state, index, action) {
  if (index !== action.polygonIndex) {
    return state;
  }
  switch (action.type) {
    case ADD_VERTEX:
      return {
        ...state,
        vertices: [...state.vertices, action.position],
      };
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

function randomInt(min, max) {
  return 0 | (min + Math.random() * (max - min));
}

function randomColor() {
  const r = randomInt(0, 255);
  const g = randomInt(0, 255);
  const b = randomInt(0, 255);
  const a = Math.random();
  return `rgba(${r}, ${g}, ${b}, ${a})`;
}
