import json
import requests


def random_postcode():
    # Requests the JSON file from the postcode API
    # The API randomly selects a new file everytime the link is requested
    r = requests.get("https://api.postcodes.io/random/postcodes")
    data = r.json()
    data = data['result']

    # Checks that the postcode generated has a valid latitude or longitude
    # Not all postcodes have a latitude and longitude on the API
    if not data['longitude'] or not data['latitude']:
        return False

    # Returns the data to the main function to use in the weather lookup function
    return data


def user_postcode(input_postcode):
    # Attempts to look up the user inputted postcode
    try:
        # Concatenated the inputted postcode to the end of the api request
        r = requests.get("https://api.postcodes.io/postcodes/" + input_postcode)
        data = r.json()
        data = data['result']
    # A key error will occur if an incorrect postcode is input
    except KeyError:
        error_message(3)
        return False

    # Checks for valid longitude or latitude
    if not data['longitude'] or not data['latitude']:
        error_message(1)
        return False

    # Returns the data to the main function to use in the weather lookup function
    return data


def weather_lookup(postcode_data):
    # Sets the latitude and longitude to string to concatenate onto the API URL
    latitude = str(postcode_data['latitude'])
    longitude = str(postcode_data['longitude'])

    # Website URL split into two different variables to reduce single line code length
    website = "https://api.open-meteo.com/v1/forecast?"
    url = website+"latitude="+latitude+"&longitude="+longitude+"&current=temperature_2m,wind_speed_10m"

    # Requests the weather JSON file from the Open Meteo API
    r = requests.get(url)
    data = r.json()

    # Saves the units and data in two different variables to display in print info
    weather_units = data['current_units']
    weather_data = data['current']

    print_info(postcode_data, weather_data, weather_units)


def print_info(postcode_data, weather_data, weather_units):
    print("\nPostcode Lookup Info")
    print("Country: {0}".format(postcode_data['country']))
    print("City: {0}".format(postcode_data['admin_district']))
    print("Postcode: {0}".format(postcode_data['postcode']))
    print("Latitude: {0}".format(postcode_data['latitude']))
    print("Longitude: {0}".format(postcode_data['longitude']))

    print("\nWeather Data Info")
    print("Time: {0}".format(weather_data['time']))
    print("Temperature: {0}{1}".format(weather_data['temperature_2m'], weather_units['temperature_2m']))
    print("Wind Speed: {0}{1}".format(weather_data['wind_speed_10m'], weather_units['wind_speed_10m']))


def error_message(number):
    # Error message uses variable contained within the function to provide more useful messages
    print("\nError Message:", number)
    if number == 1:
        print("A postcode has been entered that does not have a valid latitude and longitude.")
        print("This is an issue with the API and there is no workaround.")
        print("Please pick another postcode.\n")
    elif number == 2:
        print("You have not entered a valid number for this input.\n")
    elif number == 3:
        print("You have not entered a valid postcode.\n")


def main():
    print("Welcome to the UK Weather Forecast")
    print("Please enter an option from the following list:")
    print("1. Enter a postcode")
    print("2. Generate a random postcode")
    user_input = input()

    # Checks that a number has been entered
    try:
        user_input = int(user_input)
    except ValueError:
        error_message(2)
        return False

    # Functionality for user inputted postcodes
    if user_input == 1:
        postcode_input = input("Please enter the postcode you would like to lookup: ")
        data = user_postcode(postcode_input)
        # Forces the user to restart if there are any errors
        if not data:
            return False
        weather_lookup(data)
    # Functionality for randomly generated postcodes
    elif user_input == 2:
        data = random_postcode()
        if not data:
            data = random_postcode()
        weather_lookup(data)
    # Error checking when a wrong number is entered
    else:
        error_message(2)
        return False

    # Functionality to loop the program without having to manually start running it again
    user_loop = input("\nWould you like to lookup another postcode? (y/n) ")
    print("")

    if user_loop == "y":
        return False
    return True


# Loops the program until the user enters "y" in the main function
loop = False
while not loop:
    loop = main()
