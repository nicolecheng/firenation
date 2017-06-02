from flask import Blueprint, jsonify

utils = Blueprint('utils', __name__)

# dictionary with one key
# key is station name with underscore in place of space
@utils.route("/data/<station_id>/")
def station(station_id):
    station_name = analyze.get_station_name(station_id)
    result = info[station_name]
    return jsonify(result=result)
