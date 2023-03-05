from typing import List

import requests


class WeatherDTO:
    """
    Data Transfer Object для представления данных о погоде.
    """
    def __init__(self, location: str, temperature: float, feels_like: float, description: str, date: str):
        """
        :param location: Местоположение.
        :param temperature: Температура в градусах Цельсия.
        :param feels_like: Ощущаемая температура в градусах Цельсия.
        :param description: Описание погодных условий.
        :param date: Дата.
        """
        self.location = location
        self.temperature = temperature
        self.feels_like = feels_like
        self.description = description
        self.date = date


def get_current_weather(api_key: str, location: str) -> WeatherDTO:
    """
    Получить данные о текущей погоде.
    :param api_key: Ключ API для доступа к сервису.
    :param location: Местоположение, для которого запрашиваются данные.
    :return: Объект WeatherDTO с данными о текущей погоде.
    """
    url = f'https://api.m3o.com/v1/weather/Now?location={location}'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    temperature = data.get('temp_c', {})
    feels_like = data.get('feels_like_c', {})
    description = data.get('condition', '')
    date = data.get('date', '')
    return WeatherDTO(location, temperature, feels_like, description, date)


def get_weather_forecast(api_key: str, location: str, days: str) -> List[WeatherDTO]:
    """
    Получить прогноз погоды.
    :param api_key: Ключ API для доступа к сервису.
    :param location: Местоположение, для которого запрашивается прогноз.
    :param days: Количество дней на которое должен быть составлен прогноз погоды.
    :return: List[WeatherDTO] Список объектов WeatherDTO с данными о погоде
    """
    url = f'https://api.m3o.com/v1/weather/forecast?location={location}&days={days}'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    forecast = data.get('forecast')
    result = []
    for item in forecast:
        temperature = item.get('avg_temp_c', {})
        feels_like = item.get('feels_like_c', {})
        description = item.get('condition', '')
        date = item.get('date', '')
        result.append(WeatherDTO(location, temperature, feels_like, description, date))
    return result

