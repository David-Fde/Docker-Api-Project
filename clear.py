#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB password: ")
connection = "mongodb+srv://David-Fde:{}@api-cluster-6z1wo.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('Chats','Example_Chat_1')

with open('chats.json') as f:
    chats_json = json.load(f)
coll.insert_many(chats_json)