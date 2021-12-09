import requests
import json

def Weather(city):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=b5c61a386dd7af2a5fa1f220e41dba4d&lang=vi&q='
    # city = input('Enter the City Name :')
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data
    # print(format_add)
    # print("Weather is {0} Temperature is mininum {1} Celcius and maximum is {2} Celcius".format(
    #     json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    return format_add