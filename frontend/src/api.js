import { useFetch } from "react-async";

/**
 * Base URL at which the API endpoints can be found.
 */
const API_BASE_URL = "http://localhost:5000";

function usePostRequest(method, params) {
  return useFetch(`${API_BASE_URL}/${method}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(params),
  });
}

export function useIntersection(polygon1, polygon2) {
  return usePostRequest("get_intersection", {
    rect1: polygon1.vertices,
    rect2: polygon2.vertices,
  });
}

export function usePolygonInfo(polygon) {
  return usePostRequest("get_polygon_info", {
    polygon: polygon.vertices.map(({ x, y }) => [x, y]),
  });
}
