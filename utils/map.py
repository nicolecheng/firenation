import urllib2, json, unicodedata
import lonlat

'''
locations = [ ["40.785902", "-73.950896"], ["40.790171", "-73.947672"],
                 ["40.794809", "-73.944614"], ["40.798651", "-73.941621"],
                 ["40.804417", "-73.937265"]]
'''

locations = lonlat.get_one()

#print locations

api_key = "AIzaSyDo-o4IgKAzVyojqTjjtxoWPRBmIkpyaLo"

'''
    assumes that the first index is the origin, then uses the next index as destination
    after calculating the distance and times, makes the second index as origin and third index as destination
'''
def get_times(destinations):
    distance_time = []
    for i in range(len(destinations) - 1):
        lat_orig = destinations[i][1]
        lon_orig = destinations[i][2]

        lat_dest = destinations[i+1][1]
        lon_dest = destinations[i+1][2]

        url = "https://maps.googleapis.com/maps/api/directions/json?"
        url += "origin=" + lat_orig + "," + lon_orig
        url += "&destination=" + lat_dest + "," + lon_dest
        url += "&mode=transit&transit_mode=subway&key="
        url += api_key
        #print url

        response = urllib2.urlopen(url).read()
        d = json.loads(response)

        
##        for x in d["routes"][0]["legs"][0]:
##            print x
        
        distance = d["routes"][0]["legs"][0]["distance"]["text"]
        time = d["routes"][0]["legs"][0]["duration"]["text"]
        distance_time.append([ distance, time ])

    return distance_time

l = get_times(locations)
for i in l:
    print i

# returns the total time it takes to get from the origin to the final destination
def get_total_time(distance_times):
    total_time = 0
    for distance_time in distance_times:
        t = distance_time[1][:-4]
        unicodedata.normalize('NFKD', t).encode('ascii','ignore')
        total_time += int(t)
    return total_time

#print get_total_time(l)

# returns the total distance from the origin to the final destination
# distance is in miles
def get_total_distance(distance_times):
    #print distance_times
    total_distance = 0
    for distance_time in distance_times:
        d = distance_time[0][:-3]
        unicodedata.normalize('NFKD', d).encode('ascii','ignore')
        total_distance += float(d)
    return total_distance

#print get_total_distance(l)


