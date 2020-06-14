import React from "react";
import PropTypes from "prop-types";
import { Line } from "react-konva";

/**
 * Renders a filled polygonal contour and its vertices.
 */
export default function Polygon({ vertices }) {
  const points = vertices.flatMap(({ x, y }) => [x, y]);
  return (
    <>
      <Line
        points={points}
        fill="#00D2FF66"
        stroke="black"
        strokeWidth={3}
        closed={true}
      />
    </>
  );
}

Polygon.propTypes = {
  index: PropTypes.number,
};
