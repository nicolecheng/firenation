from google.transit import gtfs_realtime_pb2
from datetime import datetime
import urllib, urllib2, json

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib2.urlopen('http://datamine.mta.info/mta_esi.php?key=98df1a1bb43961262574931b96b28fd6&feed_id=1')
feed.ParseFromString(response.read())

STOPS = {"1": ["Van Cortlandt Park-242 Street / Broadway", "238 Street / Broadway", "231 Street / Broadway", "Marble Hill-225 Street / Broadway", "215 Street / 10 Avenue", "207 Street / 10 Avenue", "Dyckman Street / Nagle Avenue", "191 Street / Saint Nicholas Avenue", "181 Street / Saint Nicholas Avenue", "168 Street-Washington Heights / Broadway", "157 Street / Broadway", "145 Street / Broadway", "137 Street-City College / Broadway", "125 Street / Broadway", "116 Street-Columbia University / Broadway", "Cathedral Parkway (110 Street) / Broadway", "103 Street / Broadway", "96 Street / Broadway", "86 Street / Broadway", "79 Street / Broadway", "72 Street / Broadway", "66 Street-Lincoln Center / Broadway", "59 Street-Columbus Circle / Broadway", "50 Street / Broadway", "Times Square-42 Street / 7 Avenue-Broadway", "34 Street-Penn Station / 7 Avenue", "28 Street / 7 Avenue", "23 Street / 7 Avenue", "18 Street / 7 Avenue", "14 Street / 7 Avenue", "Christopher Street-Sheridan Square / 7 Avenue South", "Houston Street / Varick Street", "Canal Street / Varick Street", "Franklin Street / Varick Street", "Chambers Street / West Broadway", "Cortlandt Street / West Broadway", "Rector Street", "South Ferry"], "2": ["Wakefield-241 Street / White Plains Road", "Nereid Avenue / White Plains Road", "233 Street / White Plains Road", "225 Street / White Plains Road", "219 Street / White Plains Road", "Gun Hill Road / White Plains Road", "Burke Avenue / White Plains Road", "Allerton Avenue / White Plains Road", "Pelham Parkway / White Plains Road", "Bronx Park East / White Plains Road", "East 180 Street / Morris Park Avenue", "West Farms Square-East Tremont Avenue / Boston Road", "174 Street / Southern Boulevard", "Freeman Street / Southern Boulevard", "Simpson Street / Westchester Avenue", "Intervale Avenue / Westchester Avenue", "Prospect Avenue / Westchester Avenue", "Jackson Avenue / Westchester Avenue", "3 Avenue-149 Street", "149 Street-Grand Concourse", "135 Street / Lenox Avenue", "125 Street / Lenox Avenue", "116 Street / Lenox Avenue", "Central Park North (110 Street) / Lenox Avenue", "96 Street / Broadway", "86 Street / Broadway", "79 Street / Broadway", "72 Street / Broadway", "66 Street-Lincoln Center / Broadway", "59 Street-Columbus Circle / Broadway", "50 Street / Broadway", "Times Square-42 Street / 7 Avenue-Broadway", "34 Street-Penn Station / 7 Avenue", "28 Street / 7 Avenue", "23 Street / 7 Avenue", "18 Street / 7 Avenue", "14 Street / 7 Avenue", "Christopher Street-Sheridan Sq / 7 Avenue", "Houston Street / Varick Street", "Canal Street / Varick Street", "Franklin Street / Varick Street", "Chambers Street / West Broadway", "Park Place / Broadway", "Fulton Street / William St", "Wall Street / William Street", "Clark Street / Henry Street", "Borough Hall / Court Street-Montague Street", "Hoyt Street / Fulton Mall", "Nevins Street / Flatbush Avenue", "Atlantic Avenue / Barclays Center", "Bergen Street / Flatbush Avenue", "Grand Army Plaza / Flatbush Avenue", "Eastern Parkway-Brooklyn Museum", "Franklin Avenue / Eastern Parkway", "President Street / Nostrand Avenue", "Sterling Street / Nostrand Avenue", "Winthrop Street / Nostrand Avenue", "Church Avenue / Nostrand Avenue", "Beverly Road / Nostrand Avenue", "Newkirk Avenue / Nostrand Avenue", "Flatbush Avenue-Brooklyn College /  Nostrand Avenue"], "3": ["Harlem-148 Street / 7 Avenue", "145 Street / Lenox Avenue", "135 Street / Lenox Avenue", "125 Street / Lenox Avenue", "116 Street / Lenox Avenue", "Central Park North (110 Street) / Lenox Avenue", "96 Street /Broadway", "72 Street /Broadway", "Times Square-42 Street /7 Avenue-Broadway", "34 Street-Penn Station / 7 Avenue", "14 Street / 7 Avenue", "Chambers Street / West Broadway", "Park Place / Broadway", "Fulton Street / William St", "Wall Street / William Street", "Clark Street / Henry Street", "Borough Hall / Court Street-Montague Street", "Hoyt Street-Fulton Mall", "Nevins Street / Flatbush Avenue", "Atlantic Avenue / Barclays Center", "Bergen Street / Flatbush Avenue", "Grand Army Plaza / Flatbush Avenue", "Eastern Parkway-Brooklyn Museum", "Franklin Avenue / Eastern Parkway", "Nostrand Avenue / Eastern Parkway", "Kingston Avenue / Eastern Parkway", "Crown Heights-Utica Avenue / Eastern Parkway", "Sutter Avenue-Rutland Road / East 98 Street", "Saratoga Avenue / Livonia Avenue", "Rockaway Avenue / Livonia Avenue", "Junius Street / Livonia Avenue", "Pennsylvania Avenue / Livonia Avenue", "Van Siclen Avenue / Livonia Avenue", "New Lots Avenue / Livonia Avenue"], "4": ["Woodlawn / Jerome Avenue", "Mosholu Parkway / Jerome Avenue", "Bedford Park Boulevard-Lehman College / Jerome Avenue", "Kingsbridge Road / Jerome Avenue", "Fordham Road / Jerome Avenue", "183 Street / Jerome Avenue", "Burnside Avenue / Jerome Avenue", "176 Street / Jerome Avenue", "Mt Eden Avenue / Jerome Avenue", "170 Street / Jerome Avenue", "167 Street / River Avenue", "161 Street-Yankee Stadium / River Avenue", "149 Street-Grand Concourse", "138 Street / Grand Concourse", "125 Street / Lexington Avenue", "116 Street / Lexington Avenue", "110 Street / Lexington Avenue", "103 Street / Lexington Avenue", "96 Street / Lexington Avenue", "86 Street / Lexington Avenue", "77 Street / Lexington Avenue", "68 Street-Hunter College / Lexington Avenue", "59 Street / Lexington Avenue", "51 Street / Lexington Avenue", "Grand Central-42 Street / Lexington Avenue", "33 Street / Park Avenue South", "28 Street / Park Avenue South", "23 Street / Park Avenue South", "14 Street-Union Square / 4 Avenue", "Astor Place / 4 Avenue", "Broadway-Lafayette St / Bleecker St", "Spring Street / Lafayette Street", "Canal Street / Lafayette Street", "Brooklyn Bridge-City Hall / Centre Street", "Fulton Street / Broadway", "Wall Street / Broadway", "Bowling Green / Broadway", "Borough Hall-Court Street / Joralemon Street", "Nevins Street / Flatbush Avenue", "Atlantic Avenue / Barclays Center / Brooklyn Academy of Music", "Bergen Street / Flatbush Avenue", "Grand Army Plaza / Flatbush Avenue", "Eastern Parkway-Brooklyn Museum", "Franklin Avenue / Eastern Parkway", "Nostrand Avenue / Eastern Parkway", "Kingston Avenue / Eastern Parkway", "Crown Heights-Utica Avenue / Eastern Parkway", "Sutter Avenue-Rutland Road / East 98 Street", "Saratoga Avenue / Livonia Avenue", "Rockaway Avenue / Livonia Avenue", "Junius Street / Livonia Avenue", "Pennsylvania Avenue / Livonia Avenue", "Van Siclen Avenue / Livonia Avenue", "New Lots Avenue / Livonia Avenue"], "5": [], "6": []}

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
      time: 1494960378 (UNIX TIMESTAMP)
    }
    stop_id: "140S"
  }
}
'''
#print feed.entity[0].trip_update.stop_time_update[0].arrival.time
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

# returns the arrival time for a given entity
def get_arrival_time(entity):
    arrival_time = entity.trip_update.stop_time_update[0].arrival.time # UNIX TIME
    return datetime.utcfromtimestamp(int(arrival_time)).strftime("%H:%M:%S")

#print "Arrival Time: " + str(get_arrival_time(e))

# returns a list of all the stops for a given train
def get_stops(train):
    return STOPS[train]

#print "Stops: " + str(get_stops("1"))
#for stop in get_stops("3"):
    #print stop


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
    
#print "Trains Arriving Now: " + str(get_arriving_trains())

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
