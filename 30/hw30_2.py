# 2. Використовуючи API для погоди https://open-meteo.com/en/docs, написати програму, яка буде
# приймати від користувача назву міста і виводити поточні показники погоди в консоль.
# Для визначення координат міста можна використати open-meteo.com

import requests

city = input("Enter city name: ")
API_key = 077a496efcf5d4e780bd63a60c835410

# Function to retrieve the city's coordinates
def get_city_coordinates(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_key}'
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    return (data[0]['latitude'], data[0]['longitude'])

# Function to retrieve current weather data
def get_current_weather(city):
    coordinates = get_city_coordinates(city)
    url = f'https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}&longitude={coordinates[1]}&hourly=temperature_2m'
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    weather = data['temperature']

# Retrieve current weather data
   weather = get_current_weather(city)
#
# Display weather data
print(f'City: {city}')
print(f'Temperature: {weather["temperature"]}°C')

#     print(f'Weather Description: {current_weather["weather_description"]}')
# else:
#     print('Weather data not available for the specified city.')

#
#
