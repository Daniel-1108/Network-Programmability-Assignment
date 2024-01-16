import json
import requests


def random_postcode():
    r = requests.get("https://api.postcodes.io/random/postcodes")
    data = r.json()
    data = data['result']

    if not data['longitude'] or not data['latitude']:
        return False

    return data


def user_postcode(input_postcode):
    r = requests.get("https://api.postcodes.io/postcodes/"+input_postcode)
    data = r.json()
    data = data['result']

    if not data['longitude'] or not data['latitude']:
        return False

    return data


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
    print("City: {0}".format(postcode_data['admin_district']))
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

    if user_input == 1:
        postcode_input = input("Please enter the postcode you would like to lookup:")
        data = user_postcode(postcode_input)
        if not data:
            print("error")
            return False
        weather_lookup(data)

    elif user_input == 2:
        data = random_postcode()
        if not data:
            data = random_postcode()
        weather_lookup(data)

    user_loop = input("Would you like to lookup another postcode? (y/n) ")
    print("")
    if user_loop == "y":
        return False
    return True


loop = False
while not loop:
    loop = main()


