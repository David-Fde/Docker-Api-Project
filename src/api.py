from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from populate import db, coll
import json

@get("/")
def index():
    return dumps(coll.find())

@get("/<tipo>")
def demo2(tipo):
    return dumps(coll.find({'userName':tipo}))


run(host='0.0.0.0', port=8080)