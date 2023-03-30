import json
from pymongo import MongoClient

def collection(uri):
    client = MongoClient(uri)
    database = client["rhobs"]
    collection = database["peaple"]
    return collection

def load(uri="localhost", datapath="data.json"):
    coll = collection(uri=uri)
    with open(datapath,"r") as fp:
        data = json.load(fp)

        for person in data: 
            coll.insert_one(person) 

load(uri="mongodb://localhost:27017",datapath="C:\\Users\\gateo\\Desktop\\aze\\data.json.codechallenge.janv22.RHOBS.json")
print("done")