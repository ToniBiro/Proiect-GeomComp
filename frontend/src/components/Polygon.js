import React from "react";
import PropTypes from "prop-types";
import { Line } from "react-konva";

/**
 * Renders a filled polygonal contour and its vertices.
 */
export default function Polygon({ vertices, color, stroke }) {
  const points = vertices.flatMap(({ x, y }) => [x, y]);
  return (
    <>
      <Line
        points={points}
        fill={color}
        stroke={stroke}
        strokeWidth={3}
        closed={true}
      />
    </>
  );
}

Polygon.propTypes = {
  vertices: PropTypes.array,
  color: PropTypes.string,
};
