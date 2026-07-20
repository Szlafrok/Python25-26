import requests
from pprint import pprint

API_KEY = "cd5b3262f4a1a6071dcf78eba8229b22"

def check_coordinates(city, API_KEY):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
    shaped = response.json()
    print(response.status_code)
    pprint(shaped)
    # lat, lon, city, country
    lat = shaped[0]["lat"]
    lon = shaped[0]["lon"]
    city_ = shaped[0]["name"]
    country = shaped[0]["country"]
    print(lat, lon, city_, country)
    return lat, lon, city_, country

def current_weather(lat, lon, API_KEY):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    shaped = response.json()
    print(response.status_code)
    pprint(shaped)

    weather = shaped["weather"][0]["description"]
    temperature = shaped["main"]["temp"]
    pressure = shaped["main"]["pressure"]
    humidity = shaped["main"]["humidity"]

    return weather, temperature, pressure, humidity


city = input("Podaj miasto startowe: ")
origin = check_coordinates(city, API_KEY)
city = input("Podaj miasto docelowe: ")
destination = check_coordinates(city, API_KEY) # (lat, lon, city, country)

weather, temperature, pressure, humidity = current_weather(destination[0], destination[1], API_KEY)
print(f"Informacje o mieście {city}")
print(f"Pogoda: {weather}")
print(f"Temperatura: {temperature}")
print(f"Ciśnienie: {pressure}")
print(f"Wilgotność: {humidity}")