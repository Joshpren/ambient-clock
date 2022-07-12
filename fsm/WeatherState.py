import time
from abc import ABC
from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class WeatherState(State, ABC):
    pass

    def __init__(self,  switch_to_state_function):
        self.__switch_to_state_function = switch_to_state_function
        self.__register_for_weather_data_function = lambda data: self.__update_weather_data(data)
        self.__weather_data = []

    def start(self):
        self.service.weather_data_controller.register_three_hourely_listener(self.__register_for_weather_data_function)

    def run(self):
        self.address_leds()

    def address_leds(self):
        # for data in self.__weather_data:
        #     hour = data[0]
        #     temperature = data[1]
        #     temperature_index = int(temperature * (self.service.number_of_led/60))
        #     if(temperature_index >= 0):
        #         for index in range(temperature_index):
        #             self.__address_led_function(Diode(index, self.service.colors_controller.red(100)))
        #     else:
        #         for index in range(120, 120 + temperature_index, -1):
        #             self.__address_led_function(Diode(index, self.service.colors_controller.blue(100)))
        #
        #     hour_index = self.service.arithmetic_logic_unit.determine_index_by_hours(hour, 0)
        #     if hour >= 12:
        #         self.__address_led_function(Diode(hour_index, self.service.colors_controller.blue(100)))
        #     else:
        #         self.__address_led_function(Diode(hour_index, self.service.colors_controller.green(100)))
        #     self.__show_diodes_function()
            time.sleep(2)



    def __update_weather_data(self, weather_data):
        self.__weather_data = weather_data

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.sundial_state)

    def clear(self):
        self.service.weather_data_controller.log_off_three_hourely_listener(self.__register_for_weather_data_function)