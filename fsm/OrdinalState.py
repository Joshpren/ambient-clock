import datetime
import time
from abc import ABC

from controller.TransmissionController import TransmissionController
from entities.Color import Color
from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class OrdinalState(State, ABC):
    pass

    def __init__(self, address_led_function, show_hands_function, clear_diode_function, switch_to_state_function):
        self.__address_led_function = address_led_function
        self.__show_hands_function = show_hands_function
        self.__clear_diode_function = clear_diode_function
        self.__switch_to_state_function = switch_to_state_function
        self.__register_for_weather_data_function = lambda data: self.__update_weather_data(data)
        self.__transmission_controller = None
        self.__display_rainy_minutes = False
        self.__rainy_indices = []

    @property
    def transmission_controller(self):
        return self.__transmission_controller

    @transmission_controller.setter
    def transmission_controller(self, transmission_controller):
        self.__transmission_controller = transmission_controller

    def start(self):
        if self.__display_rainy_minutes == True:
            self.service.weather_data_controller.register_minutely_listener(self.__register_for_weather_data_function)

    def address_leds(self):
        current_time = datetime.datetime.now()
        indices = self.determine_indices(current_time)
        self.__address_led_function(Diode(indices[0], self.service.colors_controller.hour_hand_color))
        self.__address_led_function(Diode(indices[1], self.service.colors_controller.minute_hand_color))
        self.__address_led_function(Diode(indices[2], self.service.colors_controller.second_hand_color))
        if self.__transmission_controller:
            darkening, brightnening = self.__transmission_controller.transmission(current_time.microsecond)
            self.__address_led_function(Diode(indices[2]-1, Color.copy(self.service.colors_controller.second_hand_color, darkening)))
            self.__address_led_function(Diode(indices[2]+1, Color.copy(self.service.colors_controller.second_hand_color, brightnening)))
        #for index in self.__rainy_indices:
        #    self.__address_led_function(Diode(index, self.service.colors_controller.rain_color))
        self.__show_hands_function()
        time.sleep(0.015)

    def determine_indices(self, current_time):
        hour_index = self.service.arithmetic_logic_unit.determine_index_by_hours(current_time.hour, current_time.minute)
        minute_index = self.service.arithmetic_logic_unit.determine_index_by_minutes(current_time.minute, current_time.second)
        second_index = self.service.arithmetic_logic_unit.determine_index_by_seconds(current_time.second, current_time.microsecond)
        return [hour_index, minute_index, second_index]

    # Weather Data provided by the weather-data-controller will be requested. This weather data containing entries
    # for each minute which has more than a 60 percent probability of precipitation. The minute is stored on the first index of the data object.
    # The specific minute will be than displayed in a light blue color. Further more because a minute representation within the clock can be more than only
    # one led-diode. The relative section which represents one minute will be calculated and also illuuminated.
    def __update_weather_data(self, weather_data):
        self.__rainy_indices.clear()
        diodes_per_one_minute = self.service.number_of_led / 60
        for data in weather_data:
            start = int(data[0] * diodes_per_one_minute)
            end = int(start + diodes_per_one_minute)
            self.__rainy_indices.extend(range(start, end))


    def react_on_motion(self):
        self.__switch_to_state_function(StateType.sundial_state)

    def clear(self):
        self.service.weather_data_controller.log_off_minutely_listener(self.__register_for_weather_data_function)

