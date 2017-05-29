import urllib2, json

locations = [ ["40.785902", "-73.950896"], ["40.790171", "-73.947672"],
                 ["40.794809", "-73.944614"], ["40.798651", "-73.941621"],
                 ["40.804417", "-73.937265"]]

api_key = "AIzaSyDo-o4IgKAzVyojqTjjtxoWPRBmIkpyaLo"

'''
    assumes that the first index is the origin, then uses the next index as destination
    after calculating the distance and times, makes the second index as origin and third index as destination
'''
def getTimes(destinations):
    distance_time = []
    for i in range(len(destinations) - 1):
        lat_orig = destinations[i][0]
        lon_orig = destinations[i][1]

        lat_dest = destinations[i+1][0]
        lon_dest = destinations[i+1][1]

        url = "https://maps.googleapis.com/maps/api/directions/json?"
        url += "origin=" + lat_orig + "," + lon_orig
        url += "&destination=" + lat_dest + "," + lon_dest
        url += "&mode=transit&transit_mode=subway&key="
        url += api_key
        print url

        response = urllib2.urlopen(url).read()
        d = json.loads(response)

        
##        for x in d["routes"][0]["legs"][0]:
##            print x
        
        distance = d["routes"][0]["legs"][0]["distance"]["text"]
        time = d["routes"][0]["legs"][0]["duration"]["text"]
        distance_time.append([ distance, time ])

    return distance_time

l = getTimes(locations)
for i in l:
    print i
        
        

        
