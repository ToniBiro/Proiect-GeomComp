import React from "react";
import { Line } from "react-konva";

import { useDispatch, useSelector } from "react-redux";
import { setVertexPosition } from "../actions";

import Vertex from "./Vertex";

export default function Polygon({ index }) {
  const dispatch = useDispatch();
  const polygon = useSelector((state) => state[index]);

  const points = polygon.vertices.flatMap(({ x, y }) => [x, y]);

  const updatePosition = (vertexIndex, x, y) => {
    dispatch(setVertexPosition(index, vertexIndex, x, y));
  };

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
