
import requests
import json

def Forcast(city):
    api_address='http://api.openweathermap.org/data/2.5/forecast?appid=b5c61a386dd7af2a5fa1f220e41dba4d&lang=vi&q='
    
    # city = input('Enter the City Name :')
    url = api_address + city
    format_add = requests.get(url).json()
    # forecast.temperature.value
    # print(format_add)
    return format_add