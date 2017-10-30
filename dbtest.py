import pymongo
from pymongo import MongoClient
import datetime
import pprint
from steemdata import SteemData
import dateutil.parser
import json
import os
from time import sleep
from bson import Binary, Code
from bson.json_util import dumps


client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.test_database

dateStr = "2017-10-27T12:27:12.000Z"
myDatetime = dateutil.parser.parse(dateStr)

s = SteemData()

result = s.Accounts.aggregate(
[
{
    "$match": {
            "profile.location": {"$exists": "true"},
                            "last_account_update": {"$gte": myDatetime}
                 }
    },


    { 
        "$project":
        {
                "account":"$account",
                "location":"$profile.location",
                "_id":0
            }},
        {"$limit":3},
    ])

data = dumps(result)


post_id = db.steemians.insert_one(data).inserted_id
pprint.pprint(db.daniel.find_one())
print(db.collection_names(include_system_collections=False))