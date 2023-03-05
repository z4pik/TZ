# API погоды интерфейс
### Этот проект представляет собой интерфейс для доступа к API погоды с использованием Python 3.8 и requests.
#### Позволяет получать погоду в данный и момент и на N дней
### Методы
Этот интерфейс предоставляет два метода:

1) Текущая погода.
   Метод **_get_current_weather_** возвращает текущую погоду для заданного местоположения.

    **Параметры запроса:**
    - `location` - обязательный параметр, задает местоположение для получения текущей погоды.
    - `api_key` - обязательный параметр, задаёт ключ API для доступа к сервису.

2) Прогноз.
  Метод **_get_weather_forecast_** возвращает прогноз погоды на N дней
  **Параметры запроса:**
   - `location` - обязательный параметр, задает местоположение для получения текущей погоды.
   - `api_key` - обязательный параметр, задаёт ключ API для доступа к сервису.
   - `days` - обязательный параметр, задаёт количество дней на которое должен быть составлен прогноз погоды.


### Как запустить скрипт.
1) Перейти в файл **_api.py_**
2) Указать свой **API_KEY**, который можно получить при регистрации и взять его из формы **Personal Token**
3) Указать локацию **LOCATION**, по которой хотите получить прогноз погоды
4) Указать количество **DAYS**, на сколько дней должен быть составлен прогноз погоды.