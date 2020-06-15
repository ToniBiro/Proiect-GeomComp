import { useFetch } from "react-async";

/**
 * Base URL at which the API endpoints can be found.
 */
const API_BASE_URL = "http://localhost:5000";

const FETCH_OPTIONS = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
};

function encodePolygon(polygon) {
  return polygon.vertices.map(({ x, y }) => [x, y]).reverse();
}

export function computeIntersection(polygon1, polygon2) {
  const params = {
    polygon1: encodePolygon(polygon1),
    polygon2: encodePolygon(polygon2),
  };
  return fetch(`${API_BASE_URL}/get_intersection`, {
    ...FETCH_OPTIONS,
    body: JSON.stringify(params),
  }).then((res) => res.json());
}

export function usePolygonInfo(polygon) {
  const params = {
    polygon: encodePolygon(polygon),
  };
  return useFetch(`${API_BASE_URL}/get_polygon_info`, {
    ...FETCH_OPTIONS,
    body: JSON.stringify(params),
  });
}
