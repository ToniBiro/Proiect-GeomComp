from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

from prgc.dcel import DCEL
from prgc.intersect import intersect_polygons
from prgc.primitive import Vector2D
from prgc.primitive import compute_area, compute_perimeter, define_polygon_type


app = Flask(__name__)

# CORS is a required security feature to allow the front end
# to send requests to the back end.
CORS(app)


@app.route('/get_intersection', methods=['POST'])
def compute_intersection():
    """
    Computes the resulting polygon from the intersection of 2 polygons

    Accepts from POST request 2 polygons.
    Input: (json format)2 lists of points.
    e.g.
    {
            'rect1': [(0, 0), (1, 0), (1, 1), (0, 1)],
            'rect2': [(0.5, -0.25), (1.25, -0.25), (1.25, 1.5), (0.5, 1.5)]
    }

    Returns: a list of points representing the polygon formed after the intersection.
    * If there are more than 1 resulting polygon
    e.g.
    {
            'points_1': [[1, 1], [0.5, 1.0], [0.5, 0.0], [1, 0]]
            'points_2': ....
             ....
    }

    """
    dcel = DCEL()
    rect1_aux = []
    rect2_aux = []
    rect1 = []
    rect2 = []

    # read json data from input
    rect1_aux = request.get_json()['rect1']
    for i, point in enumerate(rect1_aux):
        rect1.append(Vector2D(point[0], point[1]))
    rect1 = dcel.create_face_from_points(rect1)

    rect2_aux = request.get_json()['rect2']
    for i, point in enumerate(rect2_aux):
        rect2.append(Vector2D(point[0], point[1]))
    rect2 = dcel.create_face_from_points(rect2)

    insect = intersect_polygons(dcel, rect1, rect2)

    # test prints - remove before deployment
    print(rect1_aux)
    print(len(insect))

# Extract the result
    json_resp = dict()
    for i in range(len(insect)):
        json_resp['points_' + str(i+1)] = []

    # create json response
    for i, polygon in enumerate(insect):
        for edge in polygon:
            json_resp['points_' +
                      str(i+1)].append((edge.target.point.x, edge.target.point.y))

    # print json response
    print(json_resp)

    return jsonify(json_resp)


@app.route('/get_polygon_info', methods=['POST'])
def get_polygon_info():
    """
    Returns information about a given polygon as json
    Input: A list of points
    e.g. { 'polygon' : [(0, 0), (1, 0), (1, 1), (0, 1)] }

    Returns: A dictionary wtih area, perimeter and polygon type (concave, convex)
    e.g. polygon_info = {
                                'area' : 1,
                                'perimeter' : 4,
                                'type' : 'concave'
                }
    """
    polygon_info = {
        'area': None,
        'perimeter': None,
        'type': None
    }

    polygon = []

    # read json data from input
    polygon = request.get_json()['polygon']

    # compute the information
    polygon_info['area'] = compute_area(polygon)
    polygon_info['perimeter'] = compute_perimeter(polygon)
    polygon_info['type'] = define_polygon_type(polygon)

    return jsonify(polygon_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
