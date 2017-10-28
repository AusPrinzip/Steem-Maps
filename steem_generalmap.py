from flask import Flask, jsonify, render_template, request, Response, url_for
from geopy.geocoders import Nominatim
from steemdata import SteemData
from pymongo import MongoClient
import dateutil.parser
import json
import os
from time import sleep

client = MongoClient('localhost', 27017)

geolocator = Nominatim(timeout=10)

app = Flask(__name__)



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
        #{"$limit":3},
    ])


# WE NEED TO CHECK IF AN ENTRY HAS BEEN GEOLOCATED ALREADY TO NOT OVERLOAD
data = {}  
data['people'] = [] 
for elemento in result: 
    location = geolocator.geocode(elemento["location"])
    sleep(1)
    print("sleep 1 sec")
    if hasattr(location,'latitude'):
        data['people'].append({  
            'user': elemento["account"],
            'latitude': location.latitude,
            'longitude': location.longitude
        })
    else:
        print("no lat/lng attribute")

filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), "./static/data.json")

with open(filename, 'w') as outfile: 
    outfile.write("var data = ") 
    json.dump(data, outfile)
    



@app.route('/')
def index():
    url_for('static', filename='markerclusterer.js')
    url_for('static', filename='data.json')
    url_for('static', filename='static1.png')
    url_for('static', filename='m2.png')
    url_for('static', filename='m3.png')
    return render_template('index_generalmap.html')