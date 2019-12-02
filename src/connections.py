#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json
'''
def getCollection():
    collection = input('Insert collection: ')
    return collection
#collection = getCollection()
'''
#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = "mongodb+srv://David:{}@cluster1-ylvcr.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('conversations','conversations')
