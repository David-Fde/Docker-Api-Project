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

@post('/user/<id_chat>/<user>')
def newUser(id_chat,user):
    new_id = coll.distinct("idUser")[-1] + 1
    name = str(user) 
    new_idmessage = coll.distinct("idMessage")[-1] + 1
    new_chat = int(id_chat)
    datetime= str(request.forms.get("datetime"))
    text = str(request.forms.get("text"))
    new_user = {
        "idUser": new_id,
        "userName": name,
        "idMessage": new_idmessage,
        "idChat": new_chat,
        "datetime": datetime,
        "text": text
    }
    coll.insert_one(new_user)
    print(f"{name} added to collection with id {new_id}")


run(host='0.0.0.0', port=8080)