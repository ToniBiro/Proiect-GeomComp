import React from "react";
import Vertex from "./Vertex";

export default function Vertices({ bounds, vertices, updatePosition }) {
  const dragBoundFunc = ({ x, y }) => ({
    x: clamp(x, bounds.xMin, bounds.xMax),
    y: clamp(y, bounds.yMin, bounds.yMax),
  });
  return vertices.map(({ x, y }, vertexIndex) => (
    <Vertex
      key={vertexIndex}
      x={x}
      y={y}
      dragBoundFunc={dragBoundFunc}
      onDragEnd={({ target }) =>
        updatePosition(vertexIndex, target.x(), target.y())
      }
    />
  ));
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}
