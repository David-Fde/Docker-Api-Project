import requests
import json

#user = "John Wick"
id = 0

URL = "http://localhost:8080/chat/{}".format(id)


data = requests.get(url = URL).json()

data.to_json("../output/chat", orient="records")