from flask import Blueprint, jsonify
import urllib2, json

utils = Blueprint('utils', __name__)

api_key = "AIzaSyDo-o4IgKAzVyojqTjjtxoWPRBmIkpyaLo"

# dictionary with one key
# train_name is train name (1, 2, 3, ect.)
# key is station name with underscore in place of space
@utils.route("/data/<train_name>/<station_id>/")
def station(station_id):
    station_name = analyze.get_station_name(station_id)
    result = info[station_name]
    return jsonify(result=train_dict(train_name,station_name))

# returns a string with all spaces replaced with underscores
def convert_spaces(s):
    return s.replace(" ", "_")

#print convert_spaces("does this work")

# returns the nearest train station within a 400 m radius given a latitude and longitude
def nearest_station(lat,lon):
    lat = float(lat)
    lon = float(lon)
    head = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    mid = "key=%s&location=%f,%f" % (api_key, lat, lon)
    end = "&radius=400&language=zh-TW&types=subway_station"
    new_url = head + mid + end
    page = urllib2.urlopen(new_url).read()
    
    places = json.loads(page) 
    if places['status'] == 'OK':
        for result in places['results']:
            place_id = result['place_id']
            
            head = "https://maps.googleapis.com/maps/api/place/details/"
            mid = "json?key=%s&placeid=%s" % (api_key, place_id)
            end = "&language=zh-TW"
            new_url = head + mid + end
            page = urllib2.urlopen(new_url).read()
            detail = json.loads(page)

            station = detail['result']['name']
    return station

#print nearest_station("40.718803", "-74.000193") # Canal St
#print nearest_station("40.855225", "-73.929412") # 191 St
