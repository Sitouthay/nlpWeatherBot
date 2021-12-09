import requests
import json

api_address='http://api.openweathermap.org/data/2.5/weather?appid=b5c61a386dd7af2a5fa1f220e41dba4d&lang=vi&q='
city = input('Nhập địa điểm: ')
url = api_address + city
json_data = requests.get(url).json()
data = json_data
print(data)
# print("Weather is {0} Temperature is mininum {1} Celcius and maximum is {2} Celcius".format(
#         json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))

# api_address='http://api.openweathermap.org/data/2.5/forecast?appid=b5c61a386dd7af2a5fa1f220e41dba4d&lang=vi&q='
# city = input('Enter the City Name :')
# url = api_address + city
# json_data = requests.get(url).json()
# data = json_data['list'][9]
# print(data)