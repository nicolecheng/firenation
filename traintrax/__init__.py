from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from utils import analyze, map, stations

app = Flask(__name__)
feed = analyze.get_feed()

@app.route("/", methods = ['GET', 'POST'])
def home(): 
    return render_template('home.html')

@app.route("/<train_name>/", methods = ['GET', 'POST'])
def train(train_name):
    analyze.setup()
    stops = analyze.get_stops(train_name)
    return render_template('train.html', stops = stops, train = train_name)


# dictionary with one key
# train_name is train name (1, 2, 3, ect.)
# key is station name with underscore in place of space
@app.route("/data/<train_name>/<station_id>/")
def station(train_name, station_id):
    station_name = station_id.replace("_", " ")
    result = analyze.train_dict(train_name, station_name)
    #print result
    return jsonify(result=result)

# coordinates is lat + long
# remember to split by +
@app.route("/gps/<coordinates>/", methods = ['GET', 'POST'])
def gps(coordinates):
    coor = coordinates.split("+")
    lat_orig = coor[0]
    long_orig = coor[1]
    #result = analyze.get_gps(lat,lon)
    analyze.setup()
    result = analyze.nearest_stations(lat_orig,long_orig)
    return render_template('gps.html', stops = result)


if __name__ == "__main__":
    app.debug = True
    app.run()

    
