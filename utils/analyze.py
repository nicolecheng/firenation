from google.transit import gtfs_realtime_pb2
from datetime import datetime
import urllib, urllib2, json

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=98df1a1bb43961262574931b96b28fd6&feed_id=1')
feed.ParseFromString(response.read())

e = feed.entity[0]

# returns the current feed
def get_feed():
    return feed

#print get_feed()

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

#print "Stop ID: " + str(get_stop_id(e)) 

# returns the trip id for a given entity which can be used to identify the train
def get_trip_id(entity):
    return entity.trip_update.trip.trip_id

#print "Trip ID: " + str(get_trip_id(e))

# returns the train name for a given entity which can be used to identify the train
def get_train(entity):
    trip_id = get_trip_id(entity)
    return trip_id[7]

#print "Train: " + str(get_train(e))

# returns the train direction for a given entity which can be used to identify the train
def get_direction(entity):
    trip_id = get_trip_id(entity)
    return trip_id[10]

#print "Direction: " + str(get_direction(e))

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

sid = get_stop_id(e)

# returns the station name given the stop id
def get_station_name(stop_id):
    head = "http://mtaapi.herokuapp.com/stop?id="
    new_url = head + stop_id
    page = urllib2.urlopen(new_url).read()
    d = json.loads(page)
    return d["result"]["name"]

#print "Station Name: " + str(get_station_name(sid))

'''
# sample call

mtaapi.herokuapp.com/api?id=120S

# sample call result

{
  "result": {
    "arrivals": [
      "06:30:00", 
      "08:38:00", 
      "10:45:00", 
      "12:55:30", 
      ...
      "12:34:00", 
      "15:22:00", 
      "18:10:00", 
      "20:58:00"
    ], 
    "lat": "40.793919", 
    "lon": "-73.972323", 
    "name": "96 St"
  }
}
'''

# returns the arrival time given the stop id
def get_arrival_times(stop_id):
    head = "http://mtaapi.herokuapp.com/api?id="
    new_url = head + stop_id
    page = urllib2.urlopen(new_url).read()
    d = json.loads(page)
    return d["result"]["arrivals"]
    
#print "Arrival Times: " + str(get_arrival_times(sid))

'''
# sample call

mtaapi.herokuapp.com/times?hour=10&minute=25

# sample call result

{
  "result": [
    {
      "arrival": "10:25:00", 
      "id": "D22N", 
      "lat": "40.718267", 
      "lon": "-73.993753", 
      "name": "Grand St"
    }, 
    ...
    {
      "arrival": "10:25:00", 
      "id": "H13S", 
      "lat": "40.585307", 
      "lon": "-73.820558", 
      "name": "Beach 98 St"
    }
  ]
}
'''

# returns the trains arriving given the time (hour and minute)
def get_arriving_trains():
    # returns the current time in hour:minute
    time = datetime.now().strftime("%H:%M")
    hour = time[0:2]
    minute = time[3:]
    head = "http://mtaapi.herokuapp.com/times?hour="
    end = "&minute="
    new_url = head + hour + end + minute
    page = urllib2.urlopen(new_url).read()
    d = json.loads(page)
    return d["result"]
    
print "Trains Arriving Now: " + str(get_arriving_trains())

#[[train,[stops]],[train,[stops]],...]
alltrains = []

# updates global list alltrains, containing all trains
def all_trains():    
    for i in feed.entity:
        if(len(str(i.trip_update.trip.trip_id))>1):
            train=i.trip_update.trip.trip_id
            stops=[]
            for s in i.trip_update.stop_time_update:
                stops.append(s.stop_id)
            alltrains.append([train,stops])
    #print alltrains
    #print feed.entity[0].trip_update.trip.trip_id

all_trains()

#print get_station_name(alltrains[100][1][0])

# returns a list of all stops that the trains are at
# i.e. (3,'N') = 3 train, northbound
def get_train(number,direction):
    stop_names=[]
    for t in alltrains:
        if "_"+str(number)+".."+str(direction) in t[0]:
            for s in t[1]:
                m = get_station_name(s)
                if m not in stop_names:
                    stop_names.append(m)
    return stop_names

#print get_train(1,'S')
