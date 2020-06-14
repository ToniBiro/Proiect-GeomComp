import React from "react";
import Vertex from "./Vertex";

export default function Vertices({ vertices, updatePosition }) {
  return vertices.map(({ x, y }, vertexIndex) => (
    <Vertex
      key={vertexIndex}
      x={x}
      y={y}
      onDragEnd={({ target }) =>
        updatePosition(vertexIndex, target.x(), target.y())
      }
    />
  ));
}
