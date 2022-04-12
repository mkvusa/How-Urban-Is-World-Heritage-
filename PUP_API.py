import geojson as geojson
import requests
import json
shapes = {}
for i in range(1, 1000):
    response = requests.get("http://2011.protectedurbanplanet.net/geo/dmFudG9lZ2V2b2VnZGV3YWFyZGU/json/zones/" + str(i))
    shapes[i] = response.text
    if len(response.json()["geoJSON"]["features"]) !=0:
        with open("PUP{}.txt".format(i),"w") as file:
            file.write(json.dumps(response.json()["geoJSON"]))
           # with open('pup.txt') as json_file:  # name of the text file
                #data = json.load(json_file)
           # from geojson import dump
           # with open('pup.geojson', 'w') as f:   # name of the output geojson file
            # dump(data, f)

print(shapes)

import json## exports all json files into one text file
with open("PUPall.txt","w") as file:
  file.write(json.dumps(shapes))



