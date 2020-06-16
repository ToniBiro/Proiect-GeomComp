import pytest
import json

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as test_client:
        yield test_client


def check_if_polygon_output_is_correct(server_output, hardcoded_output):
    # pair each figure from server output with a harcoded expected output
    already_verified = [False] * len(server_output)
    for fig_output in hardcoded_output:
        found = False
        for fig_server_cnt in range(len(server_output)):
            if already_verified[fig_server_cnt]:
                continue  # this one is already paired
            fig_server = server_output[fig_server_cnt]
            if fig_output == fig_server:
                found = True
                already_verified[fig_server_cnt] = True  # found his pair
                break  # no reason to continue
            # check all permutations; example: [(0,0), (1,0), (0,1)] = [(1,0), (0,1), (0,0)]
            for start_of_perm in range(1, len(fig_server)):
                if fig_output == fig_server[start_of_perm:]+fig_server[:start_of_perm]:
                    found = True
                    already_verified[fig_server_cnt] = True  # found his pair
                    break  # no reason to continue
            if found:
                break  # no reason to continue
            fig_server = server_output[fig_server_cnt][::-1]
            if fig_output == fig_server:
                found = True
                already_verified[fig_server_cnt] = True  # found his pair
                break  # no reason to continue
            # check all permutations; example: [(0,0), (1,0), (0,1)] = [(1,0), (0,1), (0,0)]
            for start_of_perm in range(1, len(fig_server)):
                if fig_output == fig_server[start_of_perm:]+fig_server[:start_of_perm]:
                    found = True
                    already_verified[fig_server_cnt] = True  # found his pair
                    break  # no reason to continue

        assert found, "the poligon " + \
            str(fig_output) + " wasn't found within server output"
    return True


def get_circular_perm(polygon):
    # given a polygonal chain, returns all permutation to the left
    # only one at a time (its an iterable)
    firstPolygon = polygon
    currentPolygon = polygon
    yield polygon
    while True:
        currentPolygon = currentPolygon[1:]+currentPolygon[:1]
        if currentPolygon == firstPolygon:
            break
        yield currentPolygon


def test_polygon_info(client):
    # all permutation of a polygonal chain shall have the same area, perimeter and type
    header = {'Content-Type': 'application/json'}
    polygon = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for polygon_perm in get_circular_perm(polygon):
        payload = {'polygon': polygon_perm}
        data = json.dumps(payload)
        rv = client.post("/get_polygon_info", data=data, headers=header)
        result = rv.json
        assert result['area'] == 1, 'Wrong area'
        assert result['perimeter'] == 4, 'Wrong perimeter'
        assert result['type'] == 'convex', 'Wrong type'


def test_polygon_intersections(client):
    # for any 2 polygonal chains, the intersection polygon shall remain the same for any circular permutation for both of the polynoms
    print("Performing Poligon Intersections Test")
    header = {'Content-Type': 'application/json'}
    polygon1 = [(0, 0), (1, 0), (1, 1), (0, 1)]
    polygon2 = [(0.5, -0.25), (1.25, -0.25), (1.25, 1.5), (0.5, 1.5)]

    for polygon1_perm in get_circular_perm(polygon1):
        for polygon2_perm in get_circular_perm(polygon2):
            payload = {
                'polygon1': polygon1_perm,
                'polygon2': polygon2_perm,
            }
            rv = client.post("/get_intersection",
                             data=json.dumps(payload), headers=header)
            result = rv.json
            assert result['length'] == 1
            assert 'polygon_0' in result
            polygon = result['polygon_0']
            expected = [[1, 1], [0.5, 1.0], [0.5, 0.0], [1, 0]]
            assert check_if_polygon_output_is_correct(
                polygon, expected), 'Wrong intersection.'
