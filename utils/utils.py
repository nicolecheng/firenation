from flask import Blueprint, jsonify

utils = Blueprint('utils', __name__)

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
