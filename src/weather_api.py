import requests
import os
from dotenv import load_dotenv

# loading environmental variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# base API endpoints
CURRENT_URL = "http://api.weatherapi.com/v1/current.json"
FORECAST_URL = "http://api.weatherapi.com/v1/forecast.json"

# function to get current weather
def get_current_weather(city):
    params = {
        'key': API_KEY,
        'q': city,
        'aqi': 'no'
    }
    response = requests.get(CURRENT_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        icon_url = data['current']['condition']['icon']
        return f"{condition}, {temp_c}°C <img src='https:{icon_url}' alt='icon'>"
    else:
        return "Error retrieving data"

# function to get weather forecast
def get_forecast(city, days=3):
    params = {
        'key': API_KEY,
        'q': city,
        'days': days,
        'aqi': 'no',
        'alerts': 'no'
    }
    response = requests.get(FORECAST_URL, params=params)
    forecast_output = []
    if response.status_code == 200:
        data = response.json()
        for day in data['forecast']['forecastday']:
            date = day['date']
            condition = day['day']['condition']['text']
            icon = day['day']['condition']['icon']
            max_temp = day['day']['maxtemp_c']
            min_temp = day['day']['mintemp_c']
            line = f"{date}: {condition}, {min_temp}°C — {max_temp}°C <img src='https:{icon}' alt='icon'>"
            forecast_output.append(line)
        return forecast_output
    else:
        return ["Error retrieving data"]
