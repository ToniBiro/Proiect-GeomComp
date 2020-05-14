import { ADD_POLYGON, SET_VERTEX_POSITION } from "./actions";

const initialState = [
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

export default function rootReducer(state = initialState, action) {
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
}

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
