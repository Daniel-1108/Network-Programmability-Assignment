import json
import requests


def random_postcode():
    r = requests.get("https://api.postcodes.io/random/postcodes")
    data = r.json()
    for postcode in data['result']:
        print(postcode, " ", data['result'][postcode])


with open('weather.json') as f:
    weatherData = json.load(f)

for weatherConditions in weatherData['weather']:
    for key in weatherConditions:
        print("{0} : {1}".format(key, weatherConditions[key]))

random_postcode()


