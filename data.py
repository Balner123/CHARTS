# data.py

import requests

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    return response.json()

def get_hourly_data(data):
    return {
        "temperature": data['hourly']['temperature_2m'],
        "humidity": data['hourly']['relative_humidity_2m'],
        "wind_speed": data['hourly']['wind_speed_10m']
    }
