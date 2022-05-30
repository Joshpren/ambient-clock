import datetime
import requests
from fsm.StateType import StateType


class WeatherState:

    API_KEY_OPEN_WEATHER = "56a81dcf3778961c19b1ce122dc8e450"
    lat = "50.865206"
    lon = "7.352614"
    exclude = "minutely"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_KEY_OPEN_WEATHER}"


    def __init__(self, address_led_function, show_diodes_function, switch_to_state_function):
        self.__address_led_function = address_led_function
        self.__show_diodes_function = show_diodes_function
        self.__switch_to_state_function = switch_to_state_function

    def address_leds(self):
        response = WeatherState.request()
        new_api_call = datetime.datetime.now().minute % 3 == 0 #500 Calls per day therefore ca. 20 calls per hour


    def determine_indices(self, current_time):
        print("Hallo")

    @classmethod
    def request(cls):
        response = requests.get(cls.url)
        print(response.text)
        return response

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.sundial_state)

WeatherState.request()