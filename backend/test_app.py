import json
import requests
from bs4 import BeautifulSoup

header = {'Content-Type':'application/json'}
payload = {
			'polygon': [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)],
		  }

r = requests.post("http://localhost:8001/get_polygon_info", data=json.dumps(payload), headers=header)

json_ = r.json()
print(json_)

# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)