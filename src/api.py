from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from populate import db, coll
import json

@get("/")
def index():
    user = input('User: ')
    return dumps(coll.find({'userName':str(user)}))

run(host='localhost', port=8080)