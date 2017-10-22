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
	# location = geolocator.geocode("San Martin de Montalban")
	# print((location.latitude, location.longitude))
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
		# print(elemento["location"])
		location = geolocator.geocode(elemento["location"])
		# elemento["location"] = location
		print((elemento["account"], elemento["location"],location.latitude, location.longitude))

	
	#variable = "asd,ewq"
	#return jsonify(result= variable)
	return jsonify(result= str(user) + str("/") + str(location.longitude) + str("/") + str(location.latitude))


@app.route('/')
def index():
    return render_template('index.html')