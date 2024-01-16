import json
import requests


def random_postcode():
    postcode_data = {}
    postcode_data['postcode'] = []
    postcode_data['country'] = []
    postcode_data['longitude'] = []
    postcode_data['latitude'] = []
    postcode_data['city'] = []

    r = requests.get("https://api.postcodes.io/random/postcodes")
    data = r.json()

    postcode_data['postcode'] = data['result']['postcode']
    postcode_data['country'] = data['result']['country']
    postcode_data['longitude'] = data['result']['longitude']
    postcode_data['latitude'] = data['result']['latitude']
    postcode_data['city'] = data['result']['admin_district']

    print(postcode_data)


def weather_info():
    with open('weather.json') as f:
        weather_data = json.load(f)

    for weatherConditions in weather_data['weather']:
        for key in weatherConditions:
            print("{0} : {1}".format(key, weatherConditions[key]))


random_postcode()


