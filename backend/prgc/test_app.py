import json
import requests

def check_if_polygon_output_is_correct(server_output, hardcoded_output):
	# TO DO...
	return bool

def test_polygon_intersections():
	
	header = {'Content-Type':'application/json'}
	payload = {
				'rect1': [(0, 0), (1, 0), (1, 1), (0, 1)],
				'rect2': [(0.5, -0.25), (1.25, -0.25), (1.25, 1.5), (0.5, 1.5)]
			  }

	r = requests.post("http://localhost:8001/get_intersection", data=json.dumps(payload), headers=header)
	print(r.text)
	correct = {'points_1': [[1, 1], [0.5, 1.0], [0.5, 0.0], [1, 0]]}
	json_ = r.json()
	assert json_ == correct, 'Wrong area, perimeter or type for given polygon.'


def test_polygon_info():
	header = {'Content-Type':'application/json'}
	payload = {
				'polygon': [(0, 0), (1, 0), (1, 1), (0, 1)],
			  }

	r = requests.post("http://localhost:8001/get_polygon_info", data=json.dumps(payload), headers=header)

	correct = {
				'area' : 1,
				'perimeter' : 4,
				'type' : 'convex'
    		}
	print(r.text)
	json_ = r.json()
	assert json_ == correct, 'Wrong area, perimeter or type for given polygon.'


test_polygon_intersections()
test_polygon_info()