from google.transit import gtfs_realtime_pb2
from time import time
import urllib, urllib2, json, math
import lonlat, map, unicodedata
from operator import itemgetter
import stations

#[[train,[stops]],[train,[stops]],...]
alltrains = []
feed = gtfs_realtime_pb2.FeedMessage()
is_feed = True

# updates global list alltrains, containing all trains
def all_trains():
    for i in feed.entity:
        if(len(str(i.trip_update.trip.trip_id))>1):
            train=i.trip_update.trip.trip_id
            stops=[]
            for s in i.trip_update.stop_time_update:
                stops.append(s.stop_id)
            alltrains.append([train,stops])

def setup():
    try:
        response = urllib2.urlopen('http://datamine.mta.info/mta_esi.php?key=3a4dc71d1253cfb47a15eb3dfa2a86a5&feed_id=1')
        # print response.read()
        feed.ParseFromString(response.read())
        all_trains()
        e = feed.entity[0]
        # print e
        # print feed
    except:
        is_feed = False

setup()

STOPS = {"1": ["Van Cortlandt Park - 242 St", "238 St", "231 St", "Marble Hill - 225 St", "215 St", "207 St", "Dyckman St", "191 St", "181 St", "168 St - Washington Hts", "157 St", "145 St", "137 St - City College", "125 St", "116 St - Columbia University", "Cathedral Pkwy", "103 St", "96 St", "86 St", "79 St", "72 St", "66 St - Lincoln Center", "59 St - Columbus Circle", "50 St", "Times Sq - 42 St", "34 St - Penn Station", "28 St", "23 St", "18 St", "14 St", "Christopher St - Sheridan Sq", "Houston St", "Canal St", "Franklin St", "Chambers St", "Cortlandt St", "Rector St", "South Ferry Loop"],
         "2": ["Wakefield - 241 St", "Nereid Av", "233 St", "225 St", "219 St", "Gun Hill Rd", "Burke Av", "Allerton Av", "Pelham Pkwy", "Bronx Park East", "E 180 St", "West Farms Sq - E Tremont Av", "174 St", "Freeman St", "Simpson St", "Intervale Av", "Prospect Av", "Jackson Av", "3 Av - 149 St", "149 St - Grand Concourse", "135 St", "125 St", "116 St", "Central Park North (110 St)", "96 St", "72 St", "Times Sq - 42 St", "34 St - Penn Station", "14 St", "Chambers St", "Park Pl", "Fulton St", "Wall St", "Clark St", "Borough Hall", "Hoyt St", "Nevins St", "Atlantic Av - Barclays Ctr", "Bergen St", "Grand Army Plaza", "Eastern Pkwy - Brooklyn Museum", "Franklin Av", "President St", "Sterling St", "Winthrop St", "Church Av", "Beverly Rd", "Newkirk Av", "Flatbush Av - Brooklyn College"],
         "3": ["Harlem - 148 St", "145 St", "135 St", "125 St", "116 St", "Central Park North (110 St)", "96 St", "72 St", "Times Sq - 42 St", "34 St - Penn Station", "14 St", "Chambers St", "Park Pl", "Fulton St", "Wall St", "Clark St", "Borough Hall", "Hoyt St", "Nevins St", "Atlantic Av - Barclays Ctr", "Bergen St", "Grand Army Plaza", "Eastern Pkwy - Brooklyn Museum", "Franklin Av", "Nostrand Av", "Kingston Av", "Crown Hts - Utica Av", "Sutter Av - Rutland Rd", "Saratoga Av", "Rockaway Av", "Junius St", "Pennsylvania Av", "Van Siclen Av", "New Lots Av"], # note: eastern parkway changed to eastern pkwy, rutland road to rutland rd, crown heights to crown hts
         "4": ["Woodlawn", "Mosholu Pkwy", "Bedford Park Blvd - Lehman College", "Kingsbridge Rd", "Fordham Rd", "183 St", "Burnside Av", "176 St", "Mt Eden Av", "170 St", "167 St", "161 St - Yankee Stadium", "149 St - Grand Concourse", "138 St - Grand Concourse", "125 St", "86 St", "59 St", "Grand Central - 42 St", "14 St - Union Sq", "Broadway-Lafayette St", "Canal St", "Brooklyn Bridge - City Hall", "Fulton St", "Wall St", "Bowling Green", "Borough Hall", "Nevins St", "Atlantic Av - Barclays Ctr", "Franklin Av", "Crown Hts - Utica Av"], # note: crown heights changed to crown hts
         "5": ["Eastchester - Dyre Av", "Baychester Av", "Gun Hill Rd", "Pelham Pkwy", "Morris Park", "E 180 St", "West Farms Sq - E Tremont Av", "174 St", "Freeman St", "Simpson St", "Intervale Av", "Prospect Av", "Jackson Av", "3 Av - 149 St", "149 St - Grand Concourse", "138 St - Grand Concourse", "125 St",
"86 St", "59 St", "Grand Central - 42 St", "14 St - Union Sq", "Brooklyn Bridge - City Hall", "Fulton St", "Wall St", "Bowling Green", "Borough Hall", "Nevins St", "Atlantic Av - Barclays Ctr", "Franklin Av", "President St", "Sterling St", "Winthrop St", "Church Av", "Beverly Rd", "Newkirk Av", "Flatbush Av - Brooklyn College"],
         "6": ["Pelham Bay Park", "Buhre Av", "Middletown Rd", "Westchester Sq - E Tremont Av", "Zerega Av", "Castle Hill Av", "Parkchester", "St Lawrence Av", "Morrison Av- Sound View", "Elder Av", "Whitlock Av", "Hunts Point Av", "Longwood Av", "E 149 St", "E 143 St - St Mary's St", "Cypress Av", "Brook Av", "3 Av - 138 St", "125 St", "116 St", "110 St", "103 St", "96 St", "86 St", "77 St", "68 St - Hunter College", "59 St", "51 St", "Grand Central - 42 St", "33 St", "28 St", "23 St", "14 St - Union Sq", "Astor Pl", "Broadway-Lafayette St", "Spring St", "Canal St", "Brooklyn Bridge - City Hall"]}


# In case GTFS doesn't load
lines456 = {'Hunts Point Av': '613', 'Bedford Park Blvd - Lehman College': '405', 'St Lawrence Av': '609', 'Burnside Av': '409', 'Eastern Pkwy - Brooklyn Museum': '238', '59 St': '629', 'Borough Hall': '423', '68 St - Hunter College': '628', 'Grand Army Plaza': '237', '103 St': '624', 'Mosholu Pkwy': '402', '77 St': '627', '23 St': '634', 'Middletown Rd': '603', 'Franklin Av': '239', 'Jackson Av': '220', 'New Lots Av': '257', 'E 149 St': '615', '110 St': '623', 'President St': '241', 'Nevins St': '234', 'Fordham Rd': '407', '138 St - Grand Concourse': '416', 'Intervale Av': '218', 'Morrison Av- Sound View': '610', 'Simpson St': '217', 'Kingsbridge Rd': '406', 'Astor Pl': '636', '96 St': '625', "E 143 St - St Mary's St": '616', 'Junius St': '254', 'Saratoga Av': '252', 'Van Siclen Av': '256', 'Westchester Sq - E Tremont Av': '604', 'Bronx Park East': '212', 'Sterling St': '242', '219 St': '207', '174 St': '215', '149 St - Grand Concourse': '415', 'Gun Hill Rd': '208', 'Pelham Pkwy': '211', 'Nereid Av': '204', 'Burke Av': '209', 'Winthrop St': '243', 'Flatbush Av - Brooklyn College': '247', 'Nostrand Av': '248', 'Pelham Bay Park': '601', 'Cypress Av': '617', 'Whitlock Av': '612', '3 Av - 149 St': '221', 'Parkchester': '608', 'Kingston Av': '249', '161 St - Yankee Stadium': '414', 'Sutter Av - Rutland Rd': '251', 'Beverly Rd': '245', '225 St': '206', '86 St': '626', 'Brooklyn Bridge - City Hall': '640', '3 Av - 138 St': '619', 'Mt Eden Av': '411', '116 St': '622', 'Bergen St': '236', '233 St': '205', 'Elder Av': '611', 'Baychester Av': '502', 'Castle Hill Av': '607', 'Brook Av': '618', '167 St': '413', '28 St': '633', 'Allerton Av': '210', 'Newkirk Av': '246', '14 St - Union Sq': '635', 'Crown Hts - Utica Av': '250', 'Spring St': '638', 'Woodlawn': '401', 'Bleecker St': '637', 'E 180 St': '213', 'Bowling Green': '420', 'West Farms Sq - E Tremont Av': '214', 'Grand Central - 42 St': '631', 'Eastchester - Dyre Av': '501', '170 St': '412', 'Rockaway Av': '253', 'Prospect Av': '219', '33 St': '632', '125 St': '621', 'Pennsylvania Av': '255', 'Church Av': '244', 'Fulton St': '418', 'Morris Park': '505', 'Atlantic Av': '235', 'Longwood Av': '614', 'Zerega Av': '606', 'Wall St': '419', '183 St': '408', 'Canal St': '639', 'Freeman St': '216', '51 St': '630', '176 St': '410', 'Buhre Av': '602'}

lines23 = {'Beverly Rd': '245', 'Christopher St - Sheridan Sq': '133', '225 St': '206', '86 St': '121', 'Bronx Park East': '212', '34 St - Penn Station': '128', 'Eastern Pkwy - Brooklyn Museum': '238', '116 St': '226', 'Bergen St': '236', '233 St': '205', '18 St': '131', 'Borough Hall': '232', '28 St': '129', 'Allerton Av': '210', 'Newkirk Av': '246', 'Times Sq - 42 St': '127', '149 St - Grand Concourse': '222', 'Crown Hts - Utica Av': '250', 'Central Park North (110 St)': '227', 'Grand Army Plaza': '237', 'Wall St': '230', 'Franklin Av': '239', 'Jackson Av': '220', '135 St': '224', 'Gun Hill Rd': '208', '145 St': '302', 'President St': '241', 'Nevins St': '234', 'West Farms Sq - E Tremont Av': '214', 'E 180 St': '213', 'Intervale Av': '218', 'Simpson St': '217', 'Wakefield - 241 St': '201', 'Hoyt St': '233', 'Houston St': '134', '96 St': '120', 'Junius St': '254', 'Franklin St': '136', 'Saratoga Av': '252', 'Nereid Av': '204', 'Rockaway Av': '253', 'Van Siclen Av': '256', 'Clark St': '231', 'Prospect Av': '219', '59 St - Columbus Circle': '125', '125 St': '225', 'Sterling St': '242', '219 St': '207', '174 St': '215', '14 St': '132', 'Pennsylvania Av': '255', 'Church Av': '244', 'New Lots Av': '257', 'Pelham Pkwy': '211', '23 St': '130', '72 St': '123', 'Harlem - 148 St': '301', 'Burke Av': '209', 'Atlantic Av': '235', 'Fulton St': '229', '50 St': '126', '66 St - Lincoln Center': '124', 'Winthrop St': '243', 'Flatbush Av - Brooklyn College': '247', 'Nostrand Av': '248', '79 St': '122', 'Chambers St': '137', 'Park Pl': '228', 'Canal St': '135', 'Freeman St': '216', '3 Av - 149 St': '221', 'Kingston Av': '249', 'Sutter Av - Rutland Rd': '251'}

line1 = {'Christopher St - Sheridan Sq': '133', '231 St': '104', '238 St': '103', '137 St - City College': '115', 'Houston St': '134', '96 St': '120', 'Cathedral Pkwy': '118', 'Franklin St': '136', '18 St': '131', '86 St': '121', '207 St': '108', 'Cortlandt St': '138', '215 St': '107', '125 St': '116', '191 St': '110', '14 St': '132', '28 St': '129', '103 St': '119', 'Times Sq - 42 St': '127', '72 St': '123', '59 St - Columbus Circle': '125', '23 St': '130', '50 St': '126', '66 St - Lincoln Center': '124', 'Chambers St': '137', '168 St - Washington Hts': '112', '79 St': '122', 'South Ferry': '140', '34 St - Penn Station': '128', 'Rector St': '139', 'Canal St': '135', 'Van Cortlandt Park - 242 St': '101', '157 St': '113', '145 St': '114', '116 St - Columbia University': '117', 'Marble Hill - 225 St': '106', '181 St': '111', 'Dyckman St': '109'}
#-------------------------------------------------------------------

#-----------------------------MTA API-------------------------------

#-------------------------------------------------------------------

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

#for i in feed.entity:
#    print i.trip_update.stop_time_update[1]#.stop_id
#print feed.entity[2]#.trip_update#.stop_time_update

def get_stop_id(entity):
    try:
        return entity.trip_update.stop_time_update[0].stop_id
    except:
        return False

#print "Stop ID: " + str(get_stop_id(e))
'''
hi = 0
while hi < len(feed.entity):
    print "Stop ID: " + str(get_stop_id(feed.entity[hi]))
    hi+=1
'''
# returns the trip id for a given entity which can be used to identify the train
def get_trip_id(entity):
    return entity.trip_update.trip.trip_id

#print "Trip ID: " + str(get_trip_id(e))

# returns the train name for a given entity which can be used to identify the train
def get_train_name(entity):
    #trip_id = get_trip_id(entity)
    #return trip_id[7]
    return entity.trip_update.trip.route_id

#print "Train: " + str(get_train_name(e))

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


# returns estimated arrival time in hour:minute:second
def get_eta(entity):
    arrival_time = get_arrival_time(entity)
    #print arrival_time
    time_now = datetime.now().strftime("%H:%M:%S")
    #print time_now
    FMT = "%H:%M:%S"
    eta = datetime.strptime(arrival_time, FMT) - datetime.strptime(time_now, FMT)
    return eta

#print "ETA: " + str(get_eta(e))


# returns a list of all the stops for a given train
def get_stops(train):
    return STOPS[str(train)]

#get_stops('3')

#print "Stops: " + str(get_stops("1"))
#for stop in get_stops("3"):
#    print stop


#-------------------------------------------------------------------

#-----------------------NYC SUBWAY DATA API-------------------------

#-------------------------------------------------------------------

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

#sid = get_stop_id(e)

# sid = "137N"

# returns the station name given the stop id
def get_station_name(stop_id):
    return stations.d[stop_id]

#print "Station Name: " + str(get_station_name('234N'))

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

# returns the estimated arrival times given the stop id
def get_etas(stop_id):
    arrival_times = get_arrival_times(stop_id)
    time_now = datetime.now().strftime("%H:%M:%S")
    FMT = "%H:%M:%S"
    etas = []
    for arrival_time in arrival_times:
        unicodedata.normalize('NFKD', arrival_time).encode('ascii','ignore')
        try:
            eta = datetime.strptime(arrival_time, FMT) - datetime.strptime(time_now, FMT)
            days, seconds = eta.days, eta.seconds
            hours = days * 24 + seconds // 3600
            minutes = (seconds % 3600) // 60
            #seconds = seconds % 60
            eta = [hours, minutes]
        except ValueError:
            pass
            '''
            arrival_time = arrival_time.replace('24','23')
            eta = datetime.strptime(arrival_time, FMT) - datetime.strptime(time_now, FMT)
            #print datetime.timedelta(hours=1)
            '''
        if hours >= 0:
            etas.append(eta)
        sorted_etas = sorted(etas, key=itemgetter(0,1))
    return sorted_etas

#print "Estimated Arrival Times for a Station: " + str(get_etas(sid))

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

# returns a list of all stops that the trains are at
# i.e. (3,'N') = 3 train, northbound
def get_train(number,direction):
    stop_names=[]
    for t in alltrains:
        if "_"+str(number)+".."+str(direction) in t[0]:
            for s in t[1]:
                m = get_station_name(s)
                #if m not in stop_names:
                stop_names.append(m)
    return stop_names

# returns both uptown and downtown trains
# [[uptown1, uptown2,...],[downtown1,downtown2,...]]
def get_trains(number):
    up = []
    down = []
    for t in alltrains:
        if "_"+str(number)+".." in t[0]:
            if "..N" in t[0]:
                for s in t[1]:
                    m = get_station_name(s)
                    up.append(m)
            elif "..S" in t[0]:
                for s in t[1]:
                    m = get_station_name(s)
                    down.append(m)
    return [up,down]

#print get_train(1,'S')
#print get_trains(1)

'''
[ [station name, {"train id": arrival time}, {"train id": arrival time}, ...] [station name, {"train id":... ] ... ]
[ ["train id", "train name", location, direction] ... ]
'''

# returns a list in the above format
def get_all_arriving_trains(train):
    stations = get_stops(train)
    new_stations = []
    trains = get_trains(train)
    uptown = trains[0]
    downtown = trains[1]
    for station in stations:
        if station in uptown:
            new_stations.append([station, "N", train])
        if station in downtown:
            new_stations.append([station, "S", train])
    new_stations = [train] + new_stations
    return new_stations

#print get_all_arriving_trains("6")

def get_distance_between_coordinates(lat_orig, long_orig, lat_dest, long_dest):
    earth_radius = 3960
    lat1_rad = math.radians(float(lat_orig))
    lat2_rad = math.radians(float(lat_dest))
    delta_lat = math.radians(float(lat_dest) - float(lat_orig))
    delta_long = math.radians(float(long_dest) - float(long_orig))

    a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_long/2) * math.sin(delta_long/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return earth_radius * c

#print get_distance_between_coordinates("40.793919", "-73.972323", "40.788644", "-73.976218")

# returns [minutes,miles] between the given stations
def get_dist(origin,destination,train_num,direction):
    line = []
    if train_num==1:
        if direction=='N':
            p=STOPS["1"]
            line=p[::-1]
            t=lonlat.get_u1()
        else:
            line=STOPS["1"]
            t=lonlat.get_d1()
    elif train_num==2:
        if direction=='N':
            p=STOPS["2"]
            line=p[::-1]
            t=lonlat.get_u2()
        else:
            line=STOPS["2"]
            t=lonlat.get_d2()
    elif train_num==3:
        if direction=='N':
            p=STOPS["3"]
            line=p[::-1]
            t=lonlat.get_u3()
        else:
            line=STOPS["3"]
            t=lonlat.get_d3()
    elif train_num==4:
        if direction=='N':
            p=STOPS["4"]
            line=p[::-1]
            t=lonlat.get_u4()
        else:
            line=STOPS["4"]
            t=lonlat.get_d4()
    elif train_num==5:
        if direction=='N':
            p=STOPS["5"]
            line=p[::-1]
            t=lonlat.get_u5()
        else:
            line=STOPS["5"]
            t=lonlat.get_d5()
    elif train_num==6:
        if direction=='N':
            p=STOPS["6"]
            line=p[::-1]
            t=lonlat.get_u6()
        else:
            line=STOPS["6"]
            t=lonlat.get_d6()
    if origin in line and destination in line:
        ori=line.index(origin)
        dest=line.index(destination)
        time=0
        distance=0.0
        while ori<dest and ori < len(t):
            minutes=t[ori][1].split()[0]
            time+=int(minutes)
            miles=t[ori][0].split()[0]
            distance+=float(miles)
            ori+=1
        return [time,distance]

#print get_dist('Van Cortlandt Park - 242 St','Marble Hill - 225 St',1,'S')
#print get_dist('Canal St','33 St',6,'N')
#print get_dist('Park Pl','145 St',3,'N')
#print get_dist('59 St','174 St',5,'N')
#print get_dist('Chambers St','34 St - Penn Station',1,'N')


def train_dict_old(train_num,station_name):
    n = get_trains(train_num)
    up = n[0]
    down = n[1]
    train_num = int(train_num)
    station_name = str(station_name)
    if train_num==1:
        train_list=STOPS["1"]
    elif train_num==2:
        train_list=STOPS["2"]
    elif train_num==3:
        train_list=STOPS["3"]
    elif train_num==4:
        train_list=STOPS["4"]
    elif train_num==5:
        train_list=STOPS["5"]
    elif train_num==6:
        train_list=STOPS["6"]
    rev=train_list[::-1]
    m = []
    for i in up:
        if i in rev and rev.index(i)<rev.index(station_name) and not(rev.index(i)==0):
            prev = rev[rev.index(i)-1]
            j=(get_dist(i,station_name,train_num,'N'))
            j.append(prev)
            j.append('uptown')
            j.append(train_num)
            if not j in m:
                m.append(j)
    for i in down:
        if i in train_list and train_list.index(i)<train_list.index(station_name) and not (train_list.index(i)==0):
            prev=train_list[train_list.index(i)-1]
            j=get_dist(i,station_name,train_num,'S')
            j.append(prev)
            j.append('downtown')
            j.append(train_num)
            if not j in m:
                m.append(j)
    return sorted(m)

def backup_feed(train_num, station_name):
    if int(train_num) == 1:
        mta_id = line1[station_name]
    elif int(train_num) < 4:
        mta_id = lines23[station_name]
    else:
        mta_id = lines456[station_name]
    now = int(round(time()))
    url = "http://apps.mta.info/trainTime/getTimesByStation.aspx?stationID=" + mta_id + "&&time=" + str(now)
    response = urllib2.urlopen(url).readlines()
    # print response

    sever_timestamp = -1

    d = {}
    l = []
    for i in response:
            i = i.strip()
            if "serverTimeStamp=" in i:
                    sever_timestamp = int(i[16:-1])
            elif "direction1[" in i:
                    data = i.split("='")[1].split(",")
                    train = data[0] if data[0][-1].lower() != "x" else data[0][:-1]
                    diff = int(data[1]) if len(data[1]) > 1 else int(data[2])
                    diff = abs(diff - sever_timestamp)/60.0
                    l.append([diff, train, "uptown"])

            elif "direction2[" in i:
                    data = i.split("='")[1].split(",")
                    train = data[0] if data[0][-1].lower() != "x" else data[0][:-1]
                    diff = int(data[1]) if len(data[1]) > 1 else int(data[2])
                    diff = abs(diff - sever_timestamp)/60.0
                    l.append([ diff, train, "downtown"])

    # print l
    d[station_name] = sorted(l)
    return d

# {'station_name':[[dist, eta, last_station_train_was_at, 'uptown'],[...],...]}
def train_dict(train_num,station_name):
    p = []
    d = {}

    # print train_num
    if is_feed:
        if int(train_num) == 1:
            l = lonlat.get_one()
        elif int(train_num) == 2:
            l = lonlat.get_two()
        elif int(train_num) == 3:
            l = lonlat.get_three()
        elif int(train_num) == 4:
            l = lonlat.get_four()
        elif int(train_num) == 5:
            l = lonlat.get_five()
        else:
            l = lonlat.get_six()
        q = lonlat.get_possible_trains(station_name, l)
        for a in q:
            k = train_dict_old(a,station_name)
            p.extend(k)

    if len(p) == 0:
        return backup_feed(train_num, station_name)

    d[station_name]= sorted(p)
    return d

#print train_dict(2,'Chambers St')

# def gps_dict(station_name):
#     q = lonlat.get_possible_trains(station_name)
#     d = {}
#     p = []
#     for a in q:
#         if is_feed:
#             k = train_dict_old(a,station_name)
#         else:
#             k = backup_feed(a, station_name)[station_name]
#         if len(k) < 1:
#             k = backup_feed(a, station_name)[station_name]
#         p.extend(k)
#
#     d[station_name]= sorted(p)
#     return d

# returns list of trains going to a particular station
def get_trains_going_to_station(station_name):
    trains = []
    for i in feed.entity:
        try:
            stop_id = get_stop_id(i)
            station = get_station_name(stop_id)
            if station == station_name:
                train = get_train_name(i)
                direction = get_direction(i)
                trains.append([train,direction])
        except:
            pass
    return trains

#print get_trains_going_to_station("Chambers St")

# identifies which train has which eta
def get_trains_at_station(station_name):
    one = ["1"]
    two = ["2"]
    three = ["3"]
    four = ["4"]
    five = ["5"]
    six = ["6"]

    if station_name in get_stops("1"):
        i1 = get_stops("1").index(station_name)
        stops1 = get_stops("1")[i1-1:i1+2]
        one += stops1
        d1 = lonlat.get_d1()[i1-1] + [stops1[0],"S","1"]
        u1 = lonlat.get_u1()[len(get_stops("1"))-i1-2] + [stops1[2],"N","1"]
        one.append(d1)
        one.append(u1)
    if station_name in get_stops("2"):
        i2 = get_stops("2").index(station_name)
        stops2 = get_stops("2")[i2-1:i2+2]
        two += stops2
        d2 = lonlat.get_d2()[i2-1] + [stops2[0],"S","2"]
        u2 = lonlat.get_u2()[len(get_stops("2"))-i2-2] + [stops2[2],"N","2"]
        two.append(d2)
        two.append(u2)
    if station_name in get_stops("3"):
        i3 = get_stops("3").index(station_name)
        stops3 = get_stops("3")[i3-1:i3+2]
        three += stops3
        d3 = lonlat.get_d3()[i3-1] + [stops3[0],"S","3"]
        u3 = lonlat.get_u3()[len(get_stops("3"))-i3-2] + [stops3[2],"N","3"]
        three.append(d3)
        three.append(u3)
    if station_name in get_stops("4"):
        i4 = get_stops("4").index(station_name)
        stops4 = get_stops("4")[i4-1:i4+2]
        four += stops4
        d4 = lonlat.get_d4()[i4-1] + [stops4[0],"S","4"]
        u4 = lonlat.get_u4()[len(get_stops("4"))-i4-2] + [stops4[2],"N","4"]
        four.append(d4)
        four.append(u4)
    if station_name in get_stops("5"):
        i5 = get_stops("5").index(station_name)
        stops5 = get_stops("5")[i5-1:i5+2]
        five += stops5
        d5 = lonlat.get_d5()[i5-1] + [stops5[0],"S","5"]
        u5 = lonlat.get_u5()[len(get_stops("5"))-i5-2] + [stops5[2],"N","5"]
        five.append(d5)
        five.append(u5)
    if station_name in get_stops("6"):
        i6 = get_stops("6").index(station_name)
        stops6 = get_stops("6")[i6-1:i6+2]
        six += stops6
        d6 = lonlat.get_d6()[i6-1] + [stops6[0],"S","6"]
        u6 = lonlat.get_u6()[len(get_stops("6"))-i6-2] + [stops6[2],"N","6"]
        six.append(d6)
        six.append(u6)

    trains = [one,two,three,four,five,six]
    #print trains
    approaching = get_trains_going_to_station(station_name)
    #print approaching

    stop_id = stations.id_from_name(station_name)
    etas = get_etas(stop_id)[:10]
    #print etas

    traveling = []
    for train in trains:
        if len(train) > 1:
            traveling.append(train[4])
            traveling.append(train[5])
    traveling = sorted(traveling, key=itemgetter(1,0))
    #print traveling

    matches = []
    for a in approaching:
        for t in traveling:
            if a[0] == t[4] and a[1] == t[3]:
                matches.append(t)
    matches = sorted(matches, key=itemgetter(0,1))

    ctr = 0
    while ctr < len(matches):
        matches[ctr][1] = etas[ctr]
        ctr += 1

    d = {station_name:matches}

    return d

#print get_trains_at_station("Chambers St")

# api_key = "AIzaSyDo-o4IgKAzVyojqTjjtxoWPRBmIkpyaLo"
# returns the nearest train station within a 400 m radius given a latitude and longitude
radius = 1
def nearest_stations(lat_orig,long_orig):
    lat_orig = float(lat_orig)
    long_orig = float(long_orig)

    all_compatible = []
    all_trains = lonlat.give_all()
    for l in all_trains:
        lat_dest = float(l[1])
        long_dest = float(l[2])
        d = get_distance_between_coordinates(lat_orig, long_orig, lat_dest, long_dest)
        # print d
        if d <= radius:
            all_compatible.append([ round(d * 100)/100, l[0], l[3][0] ])

    return sorted(all_compatible)



#print nearest_station("40.718803", "-74.000193") # Canal St
#print nearest_station("40.855225", "-73.929412") # 191 St

# returns trains arriving at the nearest station to you
def get_gps(lat,lon):
    station_name = nearest_station(lat,lon)
    trains = get_trains_at_station(station_name)
    return trains

#print get_gps("40.718803", "-74.000193")

def measureTime():
    start = time.clock()
    train_dict(5)
    elapsed = time.clock()
    elapsed = elapsed - start
    print "Time spent in (function name) is: ", elapsed
#measureTime()


'''
# {'station_name':[[dist, eta, last_station_train_was_at, 'uptown'],[...],...]}

def train_dict_old(train_num,station_name):
    #print 111111111111111111111111111111111
    n = get_trains(train_num)
    up = n[0]
    down = n[1]
    d = {}
    train_num = int(train_num)
    if train_num==1:
        train_list=STOPS["1"]
    elif train_num==2:
        train_list=STOPS["2"]
    elif train_num==3:
        train_list=STOPS["3"]
    elif train_num==4:
        train_list=STOPS["4"]
    elif train_num==5:
        train_list=STOPS["5"]
    elif train_num==6:
        train_list=STOPS["6"]
    rev=train_list[::-1]
    m = []
    for i in up:
        if i in rev and rev.index(i)<rev.index(station_name) and not(rev.index(i)==0):
            prev = rev[rev.index(i)-1]
            j=(get_dist(i,station_name,train_num,'N'))
            j.append(prev)
            j.append('uptown')
            j.append(train_num)
            if not j in m:
                m.append(j)
    for i in down:
        if i in train_list and train_list.index(i)<train_list.index(station_name) and not (train_list.index(i)==0):
            prev=train_list[train_list.index(i)-1]
            j=get_dist(i,station_name,train_num,'S')
            j.append(prev)
            j.append('downtown')
            j.append(train_num)
            if not j in m:
                m.append(j)
    d[station_name] = sorted(m)
    return d

# {'station_name':[[dist, eta, 'uptown'],[...],...]}
def train_dict1(train_num,station_name):
    n = get_trains(train_num)
    up = n[0]
    down = n[1]
    d = {}
    train_num = int(train_num)
    if train_num==1:
        train_list=STOPS["1"]
    elif train_num==2:
        train_list=STOPS["2"]
    elif train_num==3:
        train_list=STOPS["3"]
    elif train_num==4:
        train_list=STOPS["4"]
    elif train_num==5:
        train_list=STOPS["5"]
    elif train_num==6:
        train_list=STOPS["6"]
    rev=train_list[::-1]
    m = []
    for i in up:
        if i in rev and rev.index(i)<rev.index(station_name):
            j=(get_dist(i,station_name,train_num,'N'))
            j.append('uptown')
            if not j in m:
                m.append(j)
    for i in down:
        if i in train_list and train_list.index(i)<train_list.index(station_name) and not (train_list.index(i)==0):
            j=get_dist(i,station_name,train_num,'S')
            j.append('downtown')
            if not j in m:
                m.append(j)
    d[station_name] = sorted(m)
    return d
#print train_dict1(2,'Chambers St')
'''

'''
#times between stations on the 1 line going downtown
def one_down():
    times = []
    one = lonlat.get_one()
    o = 0
    d = 1
    origin = [one[o][1],[one[o][2]]]
    dest = [one[d][1],[one[d][2]]]
    while len(times) < len(one)-1:
        eta = map.get_times([origin,dest])
        times.append(eta)
        o += 1
        d += 1
        origin = [one[o][1],one[o][2]]
        dest = [one[d][1],one[d][2]]
        print origin
    return times

print one_down()
'''

'''
# returns a list of how far each station is from one another on 1 downtown train
def one_down():
    ret = map.get_times(lonlat.get_one())
    return ret

def one_up():
    u = lonlat.get_one()
    u.reverse()
    ret = map.get_times(u)
    return ret

def two_down():
    ret = map.get_times(lonlat.get_two())
    return ret

def two_up():
    u = lonlat.get_two()
    u.reverse()
    ret = map.get_times(u)
    return ret

def three_down():
    ret = map.get_times(lonlat.get_three())
    return ret

def three_up():
    u = lonlat.get_three()
    u.reverse()
    ret = map.get_times(u)
    return ret

def four_down():
    ret = map.get_times(lonlat.get_four())
    return ret

def four_up():
    u = lonlat.get_four()
    u.reverse()
    ret = map.get_times(u)
    return ret

def five_down():
    ret = map.get_times(lonlat.get_five())
    return ret

def five_up():
    u = lonlat.get_five()
    u.reverse()
    ret = map.get_times(u)
    return ret

def six_down():
    ret = map.get_times(lonlat.get_six())
    return ret

def six_up():
    u = lonlat.get_six()
    u.reverse()
    ret = map.get_times(u)
    return ret
'''
'''
def error_count(down,up):
    d = []
    u = []
    for i in down:
        d.append(i[0].split()[0])
    for i in up:
        u.append(i[0].split()[0])
    u = u[::-1]
    count = 0
    error=0
    while count < len(d):
        if not d[count] == u[count]:
            error+=1
            print str(d[count]) + " v " +str(u[count])
            print count
        count+=1
    return error
#print error_count(four_down(),four_up())
'''
'''

def write_file():
    f = open('train.txt','w')
    one=[one_down(),one_up()]
    two=[two_down(),two_up()]
    three=[three_down(),three_up()]
    four=[four_down(),four_up()]
    five=[five_down(),five_up()]
    six=[six_down(),six_up()]
    s=''
    if(error_count(one[0],one[1])):
        s+="d1="+str(one[0])+"\n\nu1="+str(one[1])
    if(error_count(two[0],two[1])):
        s+="\n\nd2="+str(two[0])+"\n\nu2="+str(two[1])
    if(error_count(three[0],three[1])):
        s+="\n\nd3="+str(three[0])+"\n\nu3="+str(three[1])
    if(error_count(four[0],four[1])):
        s+="\n\nd4="+str(four[0])+"\n\nu4="+str(four[1])
    if(error_count(five[0],five[1])):
        s+="\n\nd5="+str(five[0])+"\n\nu5="+str(five[1])
    if(error_count(six[0],six[1])):
        s+="\n\nd6="+str(six[0])+"\n\nu6="+str(six[1])
    f.write(s)
    f.close()

write_file()
'''
'''
f = open('train.txt','w')
f.write("d1="+str(one_down())+"\n\nu1="+str(one_up())+"\n\nd2="+str(two_down())+"\n\nu2="+str(two_up())+"\n\nd3="+str(three_down())+"\n\nu3="+str(three_up())+"\n\nd4="+str(four_down())+"\n\nu4="+str(four_up())+"\n\nd5="+str(five_down())+"\n\nu5="+str(five_up())+"\n\nd6="+str(six_down())+"\n\nu6="+str(six_up()))
f.close()
'''
'''
# returns the station name given the stop id
def station_names():
    head = "http://mtaapi.herokuapp.com/stations"
    page = urllib2.urlopen(head).read()
    d = json.loads(page)[result]
    f = open('stations.txt','w')
    f.write(str(d))
    f.close()
    #return d["result"]["name"]
#station_names()
'''
