import requests
import json

user = "John Wick"

URL = "http://localhost:8080/{}".format(user)


data = requests.get(url = URL).json()

print(data)