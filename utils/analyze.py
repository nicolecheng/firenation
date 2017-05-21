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

#e = feed.entity[0]
#print "Stop ID: " + str(get_stop_id(e)) 

# returns the trip id for a given entity which can be used to identify the train
def get_trip_id(entity):
    return entity.trip_update.trip.trip_id

#print "Trip ID: " + str(get_trip_id(e))

# returns the trip id for a given entity which can be used to identify the train
def get_train(entity):
    trip_id = get_trip_id(entity)
    return trip_id[7]

#print "Train: " + str(get_train(e))

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

#sid = get_stop_id(e)
#print "Station Name: " + str(get_station_name(sid))

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
