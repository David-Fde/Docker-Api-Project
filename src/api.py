from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from connections import db, coll
import json


@get("/")
def get_all():
    return dumps(coll.find())

@get("/<user>")
def get_user(user):
    return dumps(coll.find({"userName":user}))

@get("/chat/<chat_id>/list")
def get_chat(chat_id):
    return dumps(coll.find({"idChat":int(chat_id)}))

@post('/user/create')
def newUser():
    name = str(request.forms.get("name"))
    new_id = coll.distinct("idUser")[-1] + 1
    new_user = {
        "idUser": new_id,
        "userName": name
    }
    print(new_user)


run(host='0.0.0.0', port=8080)