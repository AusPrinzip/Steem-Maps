from flask import Flask, jsonify, render_template, request, Response
from geopy.geocoders import Nominatim
from steemdata import SteemData
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

geolocator = Nominatim(timeout=10)

app = Flask(__name__)

s = SteemData()

@app.route('/geolocation')
def geolocation():

	user = request.args.get('user', 0, type=str)
	s = SteemData()

	data = s.Accounts.aggregate(
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
    {"$limit":30},
	])

for elemento in data:
    # print(elemento["location"])
    location = geolocator.geocode(elemento["location"])
    if hasattr(location,'latitude'):
    # elemento["location"] = location
        print((elemento["account"], location,location.latitude, location.longitude))
    else:
        print("no lat/lng attribute")


	return jsonify(result= str(user) + str("/") + str(location.longitude) + str("/") + str(location.latitude))


@app.route('/')
def index():
    return render_template('index_simplemap.html')