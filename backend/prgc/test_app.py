import json
import requests

def check_if_polygon_output_is_correct(server_output, hardcoded_output):
	# TO DO: refactor
	assert len(server_output) == len(hardcoded_output), "Different output length"
	# pair each figure from server output with a harcoded expected output
	already_verified = [False] * len(server_output)
	for fig_output in hardcoded_output:
		found = False
		for fig_server_cnt in range(len(server_output)):
			if already_verified[fig_server_cnt]:
				continue # this one is already paired
			fig_server = server_output[fig_server_cnt]
			if fig_output == fig_server:
				found = True
				already_verified[fig_server_cnt] = True # found his pair
				break # no reason to continue
			# check all permutations; example: [(0,0), (1,0), (0,1)] = [(1,0), (0,1), (0,0)] 
			for start_of_perm in range (1, len(fig_server)):
				if fig_output == fig_server[start_of_perm:]+fig_server[:start_of_perm]:
					found = True
					already_verified[fig_server_cnt] = True # found his pair
					break # no reason to continue
			if found: 
				break # no reason to continue
			fig_server = server_output[fig_server_cnt][::-1]
			if fig_output == fig_server:
				found = True
				already_verified[fig_server_cnt] = True # found his pair
				break # no reason to continue
			# check all permutations; example: [(0,0), (1,0), (0,1)] = [(1,0), (0,1), (0,0)] 
			for start_of_perm in range (1, len(fig_server)):
				if fig_output == fig_server[start_of_perm:]+fig_server[:start_of_perm]:
					found = True
					already_verified[fig_server_cnt] = True # found his pair
					break # no reason to continue
			
		assert found == True, "the poligon " + str(fig_output) + " wasn't found within server output"
	return True

check_if_polygon_output_is_correct ([], [])

def getCircularPerm (polygon):
	# given a polygonal chain, returns all permutation to the left
	# only one at a time (its an iterable)
	firstPolygon = polygon
	currentPolygon = polygon
	yield polygon
	while True:
		currentPolygon = currentPolygon[1:]+currentPolygon[:1]
		if currentPolygon == firstPolygon: break
		yield currentPolygon

def tryGetPerm ():
	for i in getCircularPerm([(0, 0), (1, 0), (1, 1), (0, 1)]):
		print (i)

def test_polygon_info():
	# all permutation of a polygonal chain shall have the same area, perimeter and type
	print ('Performing Polygon Info Test')
	header = {'Content-Type':'application/json'}
	polygon = [(0, 0), (1, 0), (1, 1), (0, 1)]

	correct = {
				'area' : 1,
				'perimeter' : 4,
				'type' : 'convex'
    		}

	for polygonPerm in getCircularPerm(polygon):
		payload = {'polygon': polygonPerm}
		r = requests.post("http://localhost:5000/get_polygon_info", data=json.dumps(payload), headers=header)
		assert r.json() == correct, 'Wrong area, perimeter or type for given polygon.'
	
	print ('Test Polygon Info Passed')

def test_polygon_intersections():
	# for any 2 polygonal chains, the intersection polygon shall remain the same for any circular permutation for both of the polynoms
	print ("Performing Poligon Intersections Test")
	header = {'Content-Type':'application/json'}
	polygon1 = [(0, 0), (1, 0), (1, 1), (0, 1)]
	polygon2 =[(0.5, -0.25), (1.25, -0.25), (1.25, 1.5), (0.5, 1.5)]

	for poligon1Perm in getCircularPerm(polygon1):
		for poligon2Perm in getCircularPerm(polygon2):
			payload = {
						'polygon1': poligon1Perm,
						'polygon2': poligon2Perm
					}
			r = requests.post("http://localhost:5000/get_intersection", data=json.dumps(payload), headers=header)
			correct = [[1, 1], [0.5, 1.0], [0.5, 0.0], [1, 0]]
			assert check_if_polygon_output_is_correct(r.json()['polygon_0'], correct) , 'Wrong intersection.'
	print ("Test Poligon Intersections Passed")
