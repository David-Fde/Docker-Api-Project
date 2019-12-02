#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json
import os 
from dotenv import load_dotenv
load_dotenv()

connection = os.getenv("MONGODBURL")

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('conversations','conversations')
