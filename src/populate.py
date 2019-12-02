#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json
from dotenv import load_dotenv
load_dotenv()
import os

connection = os.getenv("MONGODBURL")

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll


db, coll = connectCollection('conversations','conversations')

with open('./input/chat.json') as f:
    chats_json = json.load(f)
coll.insert_many(chats_json)