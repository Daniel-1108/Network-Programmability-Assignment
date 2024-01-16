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

    return postcode_data


def weather_info():
    with open('weather.json') as f:
        weather_data = json.load(f)

    for weatherConditions in weather_data['weather']:
        for key in weatherConditions:
            print("{0} : {1}".format(key, weatherConditions[key]))


def weather_lookup(postcode_data):
    print(postcode_data)
    latitude = str(postcode_data['latitude'])
    longitude = str(postcode_data['longitude'])
    url = "https://"+"api.met.no/weatherapi/locationforecast/2.0/compact?lat="+latitude+"&lon="+longitude
    print(url)

    r = requests.get(url)
    print(r.text)
def main():
    print("Welcome to the UK Weather Forecast")
    print("Please enter an option from the following list:")
    print("1. Enter a postcode")
    print("2. Generate a random postcode")
    user_input = input()

    try:
        user_input = int(user_input)
    except ValueError:
        print("error")

    if user_input == 2:
        data = random_postcode()
        weather_lookup(data)


main()


