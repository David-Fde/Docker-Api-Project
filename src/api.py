from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from populate import db, coll
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

'''
@post('/add')
def add_user():    
    new_idUser = coll.distinct("idUser")[-1] + 1
    new_name = str(request.forms.get("userName"))
    new_idmessage = coll.distinct("idMessage")[-1] + 1
    new_idchat = coll.distinct("idChat")[-1] + 1
    new_text = coll.distinct("text")[-1] + 1
    document = {"idUser": new_idUser,
                "userName": new_name,
                "idMessage": new_idmessage,
                "idChat": new_idchat,
                "text": new_text
               }
'''
run(host='0.0.0.0', port=8080)