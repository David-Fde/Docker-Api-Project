import requests
import api
import json

URL = "http://localhost:8080"

user = "Jhon Wick"

PARAMS = {'userName': user}

r = requests.get(url = URL, params = PARAMS)

data = r.json


print(data["userName"])