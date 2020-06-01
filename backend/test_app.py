import json
import requests
from bs4 import BeautifulSoup


header = {'Content-Type':'application/json'}

payload = {
			'rect1': [(0, 0), (1, 0), (1, 1), (0, 1), (2, 0.5)],
			'rect2': [(0.5, 0), (1, 0), (1, 1.5), (0.5, 1.5)]
		}

r = requests.post("http://localhost:8001/test_intersect", data=json.dumps(payload), headers=header)
print(r.text)

# soup = BeautifulSoup(r.content, 'html.parser')

json_ = r.json()
print(json_)
# print(soup)

# print(req.json())