import React, { useState } from "react";
import { Stage, Layer } from "react-konva";

import { Provider, useDispatch, useSelector, useStore } from "react-redux";
import { addPolygon, setCurrentPolygon, addVertex } from "./actions";

import Polygon from "./components/Polygon";

export default App;

/**
 * Root application component.
 *
 * @component
 */
function App() {
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
  const polygons = useSelector((state) => state.polygons);
  const currentPolygon = useSelector((state) => state.currentPolygon);

  const [addingNewVertex, setAddingNewVertex] = useState(false);

  return (
    <>
      {addingNewVertex && <h2>Click anywhere to add a new vertex</h2>}
      {/* draw the polygons on a canvas */}
      <Stage
        width={360}
        height={360}
        onMouseDown={({ target }) => {
          if (addingNewVertex) {
            const position = target.getStage().getPointerPosition();
            dispatch(addVertex(currentPolygon, position));
            setAddingNewVertex(false);
          }
        }}
      >
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
        <button
          disabled={addingNewVertex}
          type="button"
          onClick={() => dispatch(addPolygon())}
        >
          Add new polygon
        </button>
      </div>
      {/* textual representation of the polygons */}
      <ul>
        {polygons.map((polygon, index) => (
          <li key={index}>
            Polygon #{index}
            {index !== currentPolygon ? (
              <button
                disabled={addingNewVertex}
                onClick={() => dispatch(setCurrentPolygon(index))}
                type="button"
              >
                Make current
              </button>
            ) : null}
            <ol>
              {polygon.vertices.map(({ x, y }, index) => (
                <li key={index}>
                  ({x}, {y})
                </li>
              ))}
              <li style={{ listStyleType: "none" }}>
                <button
                  disabled={addingNewVertex}
                  onClick={() => setAddingNewVertex(true)}
                  type="button"
                >
                  Add new
                </button>
              </li>
            </ol>
          </li>
        ))}
      </ul>
    </>
  );
}
