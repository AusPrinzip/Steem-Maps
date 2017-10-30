# Steem Maps

This project aims to improve geographic awareness among Steem users. By improving geographical visibility of users neighboorhoods, more meetups ands gatherings will take place.

An area distance filter will be implemented. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Please note that an Google Map API Key is not mandatory, since we are using external geolocation. Warning: Exposing your API key might be exploitable.

Pip pymongo:

```
python -m pip install pymongo
```


### Installing

Geopy

```
pip install geopy
```



## Running the tests

Currently testing manually with index_simplemap.html. (Check videoblog for more info)[https://www.youtube.com/watch?v=08cHmM8UssQ]

### Break down into end to end tests

POST html method test and backend geolocation (Use steem_simplemap.py) like explained in the videoblog.


## Deployment

tbd

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pip](https://pypi.python.org/pypi/pip) - Python Package Management
* [Pymongo](https://api.mongodb.com/python/current/) - MongoDB python library
* [Geopy](https://github.com/geopy/geopy) - Geolocator module for python
* [MongoDB](https://docs.mongodb.com/) - NoSQL Database
* [Markerclusterer](https://github.com/googlemaps/js-marker-clusterer) - Google Map API JS library for Markers clustering

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Daniel Martinez** - *Initial work* - [lightproject](https://steemit.com/@lightproject/transfers)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* @Furion thanks a lot for the great Steemdata resource
* @Gargon Appreciate your creativity, thanks for your contributions improving user searches



