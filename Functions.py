import pymongo



client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["rhobs"]
collection = db["peaple"]


male_count = collection.count_documents({"sex": "M"})


female_count = collection.count_documents({"sex": "F"})

print(f"Male count: {male_count}")
print(f"Female count: {female_count}")


def getcompany(n):
    db = client["rhobs"]
    collection = db["peaple"]
    X=collection.aggregate([
        {"$group": {"_id": "$company", "count": {"$sum": 1}}}])
    
    for z  in X:
        if(z["count"]>n):

            print(z["_id"])
getcompany(5)

def pyramid (job):

    db = client["rhobs"]
    collection = db["peaple"]

    result = collection.aggregate([
    {"$match": {"job": job}},
    {"$sort": {"birthdate": 1}}
                ])
    print(collection.find().sort ( { "birthdate", -1 } ))
    print("aa")
   
pyramid("Marie")

    
    