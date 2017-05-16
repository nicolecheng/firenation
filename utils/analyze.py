from google.transit import gtfs_realtime_pb2
import urllib, urllib2, json

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=98df1a1bb43961262574931b96b28fd6&feed_id=1')
feed.ParseFromString(response.read())

'''
# sample entity format

id: "000001"
trip_update {
  trip {
    trip_id: "082350_1..S02R"
    start_date: "20170516"
    route_id: "1"
  }
  stop_time_update {
    arrival {
      time: 1494960378
    }
    stop_id: "140S"
  }
}
'''

# returns the stop id for a given entity which can be used to identify the station
def get_stop_id(entity):
    return entity.trip_update.stop_time_update[0].stop_id

e = feed.entity[0]
print get_stop_id(e)

'''
# sample call

mtaapi.herokuapp.com/stop?id=140S

# sample call result

{
  "result": {
    "lat": "40.701411", 
    "lon": "-74.013205", 
    "name": "South Ferry Loop"
  }
}
'''

# returns the station name given the stop id
def get_station_name(stop_id):
    head = "http://mtaapi.herokuapp.com/stop?id="
    new_url = head + stop_id
    page = urllib2.urlopen(new_url).read()
    d = json.loads(page)
    return d["result"]["name"]

sid = get_stop_id(e)
print get_station_name(sid)
