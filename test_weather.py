# import json
# import requests
#
# geo_key = 'edcf7aa4-38a1-463f-a0a7-48d07be1f9ba'
# weather_key = {'X-Yandex-API-Key': 'ff78cec1-c189-433a-a7f0-fe9a05fe3c2c'}
#
#
# def get_city_coord(city):
#     payload = {'geocode': city, 'apikey': geo_key, 'format': 'json'}
#     r = requests.get('https://geocode-maps.yandex.ru/1.x', params=payload)
#     geo = json.loads(r.text)
#     return geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
#
#
# def get_weather(city):
#     coordinates = get_city_coord(city).split()
#     payload = {'lat': coordinates[1], 'lon': coordinates[0], 'lang': 'ru_RU'}
#     r = requests.get('https://api.weather.yandex.ru/v2/forecast', params=payload, headers=weather_key)
#     weather_data = json.loads(r.text)
#     return weather_data
#
# print(get_weather("Магадан"))