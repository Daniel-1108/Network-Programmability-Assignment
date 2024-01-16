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
    data = data['result']

    postcode_data['postcode'] = data['postcode']
    postcode_data['country'] = data['country']
    postcode_data['longitude'] = data['longitude']
    postcode_data['latitude'] = data['latitude']
    postcode_data['city'] = data['admin_district']

    return postcode_data


def weather_lookup(postcode_data):
    latitude = str(postcode_data['latitude'])
    longitude = str(postcode_data['longitude'])
    website = "https://api.open-meteo.com/v1/forecast?"
    url = website+"latitude="+latitude+"&longitude="+longitude+"&current=temperature_2m,wind_speed_10m"

    r = requests.get(url)
    data = r.json()
    weather_units = data['current_units']
    weather_data = data['current']

    print_info(postcode_data, weather_data, weather_units)


def print_info(postcode_data, weather_data, weather_units):
    print("")
    print("Postcode Lookup Info")
    print("Country: {0}".format(postcode_data['country']))
    print("City: {0}".format(postcode_data['city']))
    print("Postcode: {0}".format(postcode_data['postcode']))
    print("Latitude: {0}".format(postcode_data['latitude']))
    print("Longitude: {0}".format(postcode_data['longitude']))

    print("")
    print("Weather Data Info")
    print("Time: {0}".format(weather_data['time']))
    print("Temperature: {0}{1}".format(weather_data['temperature_2m'], weather_units['temperature_2m']))
    print("Wind Speed: {0}{1}".format(weather_data['wind_speed_10m'], weather_units['wind_speed_10m']))


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


