from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from connections import db, coll
import json
import datetime
import functions as fnc


@get("/")
def get_all():
    return dumps(coll.find())

@get("/<user>")
def get_user(user):
    return dumps(coll.find({"userName":user}))

@get("/chat/<chat_id>/list")
def get_chat(chat_id):
    return dumps(coll.find({"idChat":int(chat_id)}))

@get("/chat/<chat_id>/sentiment")
def get_sentiment(chat_id):
    return fnc.sentiment(get_chat(chat_id))

@get("/user/<user_id>/recommend")
def get_recommendation(user_id):    
    return fnc.recommendation(user_id,get_all())

@post('/user/create')
def new_user():
    new_id = coll.distinct("idUser")[-1] + 1  
    name = str(request.forms.get("userName"))  
    date = str(datetime.datetime.now())
    print(f"User {name} added with id {new_id}")
    new_user = {
        "idUser": new_id,
        "userName": name,        
        "datetime": date
    }
    coll.insert_one(new_user)


@post('/chat/create')
def new_chat():
    chatId= int(request.forms.get("idChat"))
    print(f"Chat added with id {chatId}")
    new_chat = {
        "idChat": chatId,                
    }
    coll.insert_one(new_chat)

@post('/chat/<chat_id>/addmessage')
def new_message(chat_id):
    new_id_message = coll.distinct("idMessage")[-1] + 1
    chatId = int(chat_id)
    new_text = str(request.forms.get("text"))
    print(f"New message added with Id: {new_id_message}")
    new_message = {
        "idMessage": new_id_message,
        "idChat" : chatId,
        "text": new_text                
    }
    coll.insert_one(new_message)

run(host='0.0.0.0', port=8080)