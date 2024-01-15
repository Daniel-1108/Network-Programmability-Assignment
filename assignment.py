import json

with open('weather.json') as f:
    weatherData = json.load(f)

for weatherConditions in weatherData['weather']:
    for key in weatherConditions:
        print("{0} : {1}".format(key, weatherConditions[key]))
