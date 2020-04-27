import React from "react";
import { Stage, Layer, Line, Circle } from "react-konva";

import { Provider, useDispatch, useSelector, useStore } from "react-redux";
import { addPolygon, setVertexPosition } from "./store";

export default function App() {
  return (
    <>
      <h1>Intersecție de poligoane</h1>
      <PolygonDisplay />
    </>
  );
}

function PolygonDisplay() {
  const store = useStore();
  const dispatch = useDispatch();
  const polygons = useSelector((state) => state);

  return (
    <>
      {/* draw the polygons on a canvas */}
      <Stage width={360} height={360}>
        <Provider store={store}>
          <Layer>
            {polygons.map((_, index) => (
              <Polygon key={index} index={index} />
            ))}
          </Layer>
        </Provider>
      </Stage>
      {/* user controls */}
      <div>
        <button type="button" onClick={() => dispatch(addPolygon())}>
          Add new polygon
        </button>
      </div>
      {/* textual representation of the polygons */}
      <ul>
        {polygons.map((polygon, index) => (
          <li key={index}>
            Polygon #{index}
            <ol>
              {polygon.vertices.map(({ x, y }, index) => (
                <li key={index}>
                  ({x}, {y})
                </li>
              ))}
            </ol>
          </li>
        ))}
      </ul>
    </>
  );
}

function Polygon({ index }) {
  const dispatch = useDispatch();
  const polygon = useSelector((state) => state[index]);

  const points = polygon.vertices.flatMap(({ x, y }) => [x, y]);

  const updatePosition = (vertexIndex, x, y) => {
    dispatch(setVertexPosition(index, vertexIndex, x, y));
  };

  // TODO: wrap in a Konva group
  return (
    <>
      <Line
        points={points}
        fill="#00D2FF66"
        stroke="black"
        strokeWidth={3}
        closed={true}
      />
      {polygon.vertices.map(({ x, y }, vertexIndex) => (
        <Vertex
          key={vertexIndex}
          x={x}
          y={y}
          onDragEnd={({ target }) =>
            updatePosition(vertexIndex, target.x(), target.y())
          }
        />
      ))}
    </>
  );
}

function Vertex({ x, y, onDragEnd }) {
  return (
    <Circle
      x={x}
      y={y}
      radius={10}
      fill="red"
      draggable={true}
      onDragEnd={onDragEnd}
    />
  );
}
