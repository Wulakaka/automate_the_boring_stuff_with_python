#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = '6b5365144319e2f05328e89c75becaea'

import json, requests, sys

# Compute location from command line arguments.

if len(sys.argv) < 3:
    print('Usage: getOpenWeather.py latitude longitude')
    sys.exit()
lat = sys.argv[1]
lon = sys.argv[2]

# Download the JSON data from OpenWeatherMap.org 's API.
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
url = 'https://api.openweathermap.org/data/3.0/onecall?lat=%s&lon=%s&appid=%s' % (lat, lon, APPID)

response = requests.get(url)
response.raise_for_status()

# print(response.text)
# Load JSON data into a python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
