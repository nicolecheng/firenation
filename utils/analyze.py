from google.transit import gtfs_realtime_pb2
from datetime import datetime
import urllib, urllib2, json
import lonlat,map

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib2.urlopen('http://datamine.mta.info/mta_esi.php?key=98df1a1bb43961262574931b96b28fd6&feed_id=1')
feed.ParseFromString(response.read())

STOPS = {"1": ["Van Cortlandt Park - 242 St", "238 St", "231 St", "Marble Hill - 225 St", "215 St", "207 St", "Dyckman St", "191 St", "181 St", "168 St - Washington Hts", "157 St", "145 St", "137 St - City College", "125 St", "116 St - Columbia University", "Cathedral Pkwy", "103 St", "96 St", "86 St", "79 St", "72 St", "66 St - Lincoln Center", "59 St - Columbus Circle", "50 St", "Times Sq - 42 St", "34 St - Penn Station", "28 St", "23 St", "18 St", "14 St", "Christopher St - Sheridan Sq", "Houston St", "Canal St", "Franklin St", "Chambers St", "Cortlandt St", "Rector St", "South Ferry Loop"],
         "2": ["Wakefield - 241 St", "Nereid Av", "233 St", "225 St", "219 St", "Gun Hill Rd", "Burke Av", "Allerton Av", "Pelham Pkwy", "Bronx Park East", "E 180 St", "West Farms Sq - E Tremont Av", "174 St", "Freeman St", "Simpson St", "Intervale Av", "Prospect Av", "Jackson Av", "3 Av - 149 St", "149 St - Grand Concourse", "135 St", "125 St", "116 St", "Central Park North (110 St)", "96 St", "72 St", "Times Sq - 42 St", "34 St - Penn Station", "14 St", "Chambers St", "Park Pl", "Fulton St", "Wall St", "Clark St", "Borough Hall", "Hoyt St", "Nevins St", "Atlantic Av - Barclays Ctr", "Bergen St", "Grand Army Plaza", "Eastern Pkwy - Brooklyn Museum", "Franklin Av", "President St", "Sterling St", "Winthrop St", "Church Av", "Beverly Rd", "Newkirk Av", "Flatbush Av - Brooklyn College"],
         "3": ["Harlem - 148 St", "145 St", "135 St", "125 St", "116 St", "Central Park North (110 St)", "96 St", "72 St", "Times Sq - 42 St", "34 St - Penn Station", "14 St", "Chambers St", "Park Pl", "Fulton St", "Wall St", "Clark St", "Borough Hall", "Hoyt St", "Nevins St", "Atlantic Av - Barclays Ctr", "Bergen St", "Grand Army Plaza", "Eastern Parkway - Brooklyn Museum", "Franklin Av", "Nostrand Av", "Kingston Av", "Crown Heights - Utica Av", "Sutter Av - Rutland Road", "Saratoga Av", "Rockaway Av", "Junius St", "Pennsylvania Av", "Van Siclen Av", "New Lots Av"],
         "4": ["Woodlawn", "Mosholu Pkwy", "Bedford Park Blvd - Lehman College", "Kingsbridge Rd", "Fordham Rd", "183 St", "Burnside Av", "176 St", "Mt Eden Av", "170 St", "167 St", "161 St - Yankee Stadium", "149 St - Grand Concourse", "138 St - Grand Concourse", "125 St", "86 St", "59 St", "Grand Central - 42 St", "14 St - Union Sq", "Brooklyn Bridge - City Hall", "Fulton St", "Wall St", "Bowling Green", "Borough Hall", "Nevins St", "Atlantic Av - Barclays Ctr", "Franklin Av", "Crown Heights - Utica Av"],
         "5": ["Eastchester - Dyre Av", "Baychester Av", "Gun Hill Rd", "Pelham Pkwy", "Morris Park", "E 180 St", "West Farms Sq - E Tremont Av", "174 St", "Freeman St", "Simpson St", "Intervale Av", "Prospect Av", "Jackson Av", "3 Av - 149 St", "149 St - Grand Concourse", "135 St", "125 St", 
"86 St", "59 St", "Grand Central - 42 St", "14 St - Union Sq", "Brooklyn Bridge - City Hall", "Fulton St", "Wall St", "Bowling Green", "Borough Hall", "Nevins St", "Atlantic Av - Barclays Ctr", "Franklin Av", "President St", "Sterling St", "Winthrop St", "Church Av", "Beverly Rd", "Newkirk Av", "Flatbush Av - Brooklyn College"],
         "6": ["Pelham Bay Park", "Buhre Av", "Middletown Rd", "Westchester Sq - E Tremont Av", "Zerega Av", "Castle Hill Av", "Parkchester", "St Lawrence Av", "Morrison Av- Sound View", "Elder Av", "Whitlock Av", "Hunts Point Av", "Longwood Av", "E 149 St", "E 143 St - St Mary's St", "Cypress Av", "Brook Av", "3 Av - 138 St", "125 St", "116 St", "110 St", "103 St", "96 St", "86 St", "77 St", "68 St - Hunter College", "59 St", "51 St", "Grand Central - 42 St", "33 St", "28 St", "23 St", "14 St - Union Sq", "Astor Pl", "Broadway-Lafayette St", "Spring St", "Canal St", "Brooklyn Bridge - City Hall"]}

e = feed.entity[0]

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

#print alltrains

#print get_station_name(alltrains[100][1][0])

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
                    #if m not in up:
                    up.append(m)
            elif "..S" in t[0]:
                for s in t[1]:
                    m = get_station_name(s)
                    #if m not in down:
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
    ori=line.index(origin)
    dest=line.index(destination)
    time=0
    distance=0.0
    while ori<dest:
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

# {'station_name':[[dist, eta, last_station_train_was_at, 'uptown'],[...],...]}

def train_dict(train_num,station_name):
    n = get_trains(train_num)
    up = n[0]
    down = n[1]
    d = {}
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
            if not j in m:
                m.append(j)
    for i in down:
        if i in train_list and train_list.index(i)<train_list.index(station_name) and not (train_list.index(i)==0):
            prev=train_list[train_list.index(i)-1]
            j=get_dist(i,station_name,train_num,'S')
            j.append(prev)
            j.append('downtown')
            if not j in m:
                m.append(j)
    d[station_name] = sorted(m)
    return d
#print train_dict(2,'Chambers St')

'''
# {'station_name':[[dist, eta, last_station_train_was_at, 'uptown'],[...],...], ...}

def train_dict(train_num):
    n = get_trains(train_num)
    up = n[0]
    down = n[1]
    d = {}
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
    for stop in train_list:
        m = []
        for i in up:
            if rev.index(i)<rev.index(stop) and not(rev.index(i)==0):
                prev = rev[rev.index(i)-1]
                j=(get_dist(i,stop,train_num,'N'))
                j.append(prev)
                j.append('uptown')
                m.append(j)
        for i in down:
            if train_list.index(i)<train_list.index(stop) and not (train_list.index(i)==0):
                prev=train_list[train_list.index(i)-1]
                j=get_dist(i,stop,train_num,'S')
                j.append(prev)
                j.append('downtown')
                m.append(j)
        d[stop] = m
    return d
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
