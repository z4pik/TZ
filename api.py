from main import *


# Укажите ваш api ключ
API_KEY = ''
# Укажите Локацию
LOCATION = 'USA'
# Укажите, на сколько дней должен быть составлен прогноз погоды.
DAYS = '7'

current_weather = get_current_weather(API_KEY, LOCATION)
print(f'Текущая температура в {current_weather.location}: {current_weather.temperature}°C')
print(f'Ощущаемая температура: {current_weather.feels_like}°C')
print(f'Описание погоды: {current_weather.description}')

weather_forecast = get_weather_forecast(API_KEY, LOCATION, DAYS)
for weather in weather_forecast:
    print(f'Дата: {weather.date}, Средняя температура: {weather.temperature}°C, '
          f'Описание погоды: {weather.description}')
