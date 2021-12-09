# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from weather import Weather
from forcast import Forcast

class action_weather_api(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.latest_message['text']
        data = Weather(location)
        temp1 = data['weather'][0]['description']
        temp2 = int(data['main']['temp']-273)
        temp3 = int(data['main']['temp_max']-272)
        iconcode = data['weather'][0]['icon']
        iconurl = 'https://openweathermap.org/img/wn/' + iconcode + '@2x.png'
        dispatcher.utter_message(text = 'Ở ' + location + ' hôm nay có '+ temp1 + '\nnhiệt độ ' + str(temp2) +  '°C và có thể tăng lên đến ' + str(temp3) + '°C', image=iconurl)
        # dispatcher.utter_message(image=iconurl)
        return []

class action_weather_city(Action):

    def name(self) -> Text:
        return "action_weather_city"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = next(tracker.get_latest_entity_values("city"), None)
        data = Weather(location)
        temp1 = data['weather'][0]['description']
        temp2 = int(data['main']['temp']-273)
        temp3 = int(data['main']['temp_max']-272)
        dispatcher.utter_message(text = 'Ở ' + location + ' hôm nay có '+ temp1 + '\nnhiệt độ ' + str(temp2) +  '°C và có thể tăng lên đến ' + str(temp3) + '°C')
        # dispatcher.utter_message(image=iconurl)
        return []


# class action_weather_recommend(Action):

#     def name(self) -> Text:
#         return "action_weather_recommend"

#     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         location = tracker.latest_message['text']
#         data = Forcast(location)
#         temp1 = data['list'][0]['weather'][0]['main']
#         temp2 = data['list'][0]['weather'][0]['description']
#         temp3 = int(data['list'][9]['main']['temp'] - 273)
#         if(str(temp1) == 'Rain'):
#             text = "Hôm nay trời có mưa nhé! " + temp2 + ', nếu đi ra ngoài bạn nhớ mang theo cái dù hoặc áo mưa nhé'
#         elif(temp3 < 20):
#             text = "Hôm nay nhiệt độ thấp hơn 20°C nhé trời lạnh lắm nhé, nhớ mặc áo lạnh để tránh trường hợp bị đau ốm nhé "
#         else:
#             text = "Hôm nay thời tiết thật đẹp! bạn muốn làm gì thì làm đi"

#         dispatcher.utter_message(text)
#         return []

class forcast_weather(Action):

    def name(self) -> Text:
        return "forcast_weather_api"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        location = next(tracker.get_latest_entity_values("city"), None)
        entity = next(tracker.get_latest_entity_values("day"), None)
        data = Forcast(location)
        # forecast.temperature.value
        day1 = ['ngày mai','1 ngày', 'mai']
        day2 = ['ngày mốt','2 ngày', 'mốt']
        
        if(entity in day1):
            wx = data['list'][9]['weather'][0]['main']
            tempmin = int(data['list'][9]['main']['temp'] - 273)
            temp2 = data['list'][9]['weather'][0]['description']
            text = 'Ngày mai ở ' + location + ' sẽ có ' + temp2 + ', có nhiệt độ từ ' + str(tempmin) + '°C'
        elif(entity in day2):
            wx = data['list'][18]['weather'][0]['main']
            tempmin = int(data['list'][18]['main']['temp'] - 273)
            temp2 = data['list'][18]['weather'][0]['description']
            text = 'Ngày mốt ở ' + location + ' sẽ có ' + temp2 + ', có nhiệt độ từ ' + str(tempmin)+ '°C'
        elif(entity == '3 ngày'):
            wx = data['list'][27]['weather'][0]['main']
            tempmin = int(data['list'][27]['main']['temp'] - 273)
            temp2 = data['list'][27]['weather'][0]['description']
            text = '3 ngày nữa ở ' + location + ' sẽ có ' + temp2 + ', có nhiệt độ từ ' + str(tempmin)+ '°C'
        elif(entity == '4 ngày'):
            wx = data['list'][36]['weather'][0]['main']
            tempmin = int(data['list'][36]['main']['temp'] - 273)
            temp2 = data['list'][36]['weather'][0]['description']
            text = '4 ngày nữa ở ' + location + ' sẽ có ' + temp2 + ', có nhiệt độ từ ' + str(tempmin)+ '°C'
        elif(entity == '5 ngày'):
            wx = data['list'][39]['weather'][0]['main']
            tempmin = int(data['list'][39]['main']['temp'] - 273)
            temp2 = data['list'][39]['weather'][0]['description']
            text = 'trong vòng 5 ngày ở ' + location + ' sẽ có ' + temp2 + ', có nhiệt độ từ ' + str(tempmin)+ '°C'

        
        dispatcher.utter_message(text)
        if(str(wx) == 'Rain'):
            text2 = "nếu bạn có đi ra ngoài bạn nên mang theo cái dù hoặc áo mưa nhé"
        elif(str(wx) == 'Clouds'):
            if(tempmin < 22):
                text2 = "Hôm nay hơi lạnh nhớ mặc áo lạnh để tránh trường hợp bị đau ốm nhé"
            else:
                text2 = "Hôm nay ở " + location + "thời tiết thật đẹp! bạn có thể đi chơi, đi du lịch thoải mãi nhé"   
        else:
            text2 = ""

        dispatcher.utter_message(text2)
        return []




# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
