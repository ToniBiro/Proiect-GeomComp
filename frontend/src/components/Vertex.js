import React from "react";
import { Circle } from "react-konva";

export default function Vertex({ x, y, onDragEnd }) {
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
