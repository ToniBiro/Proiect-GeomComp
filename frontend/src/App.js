import React, { useState } from "react";
import { Stage, Layer, Line, Circle } from "react-konva";

export default function App() {
  return (
    <>
      <h1>Intersecție de poligoane</h1>
      <PolygonDisplay />
    </>
  );
}

const initialPolygons = [
  {
    id: 0,
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

function PolygonDisplay() {
  const [polygonData, setPolygonData] = useState(initialPolygons);

  console.log("redrawing polygon display");

  const updatePosition = (polygonIndex, vertexIndex, x, y) => {
    const dataCopy = JSON.parse(JSON.stringify(polygonData));
    dataCopy[polygonIndex].vertices[vertexIndex] = { x, y };
    setPolygonData(dataCopy);
  };

  return (
    <>
      {/* draw the polygons on a canvas */}
      <Stage width={360} height={360}>
        <Layer>
          {polygonData.map((polygon) => (
            <Polygon
              key={polygon.id}
              points={polygon.vertices.flatMap(({ x, y }) => [x, y])}
            />
          ))}
        </Layer>
        <Layer>
          {polygonData.flatMap((polygon, polygonIndex) =>
            polygon.vertices.map(({ x, y }, vertexIndex) => (
              <Vertex
                key={`${polygon.id}_${vertexIndex}`}
                x={x}
                y={y}
                onDragEnd={({ target }) =>
                  updatePosition(
                    polygonIndex,
                    vertexIndex,
                    target.x(),
                    target.y()
                  )
                }
              />
            ))
          )}
        </Layer>
      </Stage>
      {/* textual representation of the polygons */}
      <ul>
        {polygonData.map((polygon, index) => (
          <li>
            Polygon #{index}
            <ol>
              {polygon.vertices.map(({ x, y }) => (
                <li>
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

function Vertex({ x, y, onDragEnd }) {
  console.log("drawing vertex at " + x + " " + y);
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

function Polygon({ points }) {
  return (
    <Line
      points={points}
      fill="#00D2FF66"
      stroke="black"
      strokeWidth={3}
      closed={true}
    />
  );
}
