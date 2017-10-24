from flask import Flask, jsonify, render_template, request, Response
from geopy.geocoders import Nominatim
from steemdata import SteemData
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

geolocator = Nominatim()

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
	            "name": user
	        }
	    },


	    { 
	    "$project":
	    {
	        "account":"$account",
	        "location":"$profile.location",
	        "_id":0
	    }},
	    {"$limit":1},
	])

	for elemento in data:

		location = geolocator.geocode(elemento["location"])

		print((elemento["account"], elemento["location"],location.latitude, location.longitude))


	return jsonify(result= str(user) + str("/") + str(location.longitude) + str("/") + str(location.latitude))


@app.route('/')
def index():
    return render_template('index_simplemap.html')