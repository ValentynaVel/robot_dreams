import requests

API_key = 'bb9afbcf5556e45bba9c7109de792691'
city_name = input("Enter city name: ")

# function to get coordinates of a city
def get_city_coordinates(city_name):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            return data[0]['lat'], data[0]['lon']
        return None

# function to get the hourly weather in the city
def get_current_weather(city_name):
    coordinates = get_city_coordinates(city_name)
    if coordinates is not None:
        lat, lon = coordinates
        url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current_weather = data['hourly']
            print(f"Hourly temperature in {city_name}: {current_weather['temperature_2m']}°C")
            return
    print("Error")

get_current_weather(city_name)