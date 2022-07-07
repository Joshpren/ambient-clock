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

    current_indices = [0, 0, 0]

    def __init__(self, switch_to_state_function):
        self.__switch_to_state_function = switch_to_state_function
        self.__indices_to_address = {}
        self.__register_for_weather_data_function = lambda data: self.__update_weather_data(data)
        self.__transmission_controller = TransmissionController(120)
        self.__display_rainy_minutes = True
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
        self.__insert(self.determine_indices(current_time))
        for diode in self.__indices_to_address.values():
            self.service.led_event_handler.address_diode(diode)
        self.service.led_event_handler.show()
        self.__indices_to_address.clear()
        time.sleep(0.5)

        #if self.__transmission_controller:
         #   darkening, brightnening = self.__transmission_controller.seconds_transmission(current_time.second,current_time.microsecond, self.service.colors_controller.second_hand_color.brightness)
          #  self.__address_led_function(Diode(self.second_hand_index, Color.copy(self.service.colors_controller.second_hand_color, darkening)))
           # self.__address_led_function(Diode(self.second_hand_index+1, Color.copy(self.service.colors_controller.second_hand_color, brightnening)))
           # print(darkening, brightnening)
        #else:
        #    self.__address_led_function(Diode(indices[2], self.service.colors_controller.second_hand_color))
        #for index in self.__rainy_indices:
        #    self.__address_led_function(Diode(index, self.service.colors_controller.rain_color))


    def determine_indices(self, current_time):
        hour_hand_index = self.service.arithmetic_logic_unit.determine_index_by_hours(current_time.hour, current_time.minute)
        minute_hand_index = self.service.arithmetic_logic_unit.determine_index_by_minutes(current_time.minute, current_time.second)
        second_hand_index = self.service.arithmetic_logic_unit.determine_index_by_seconds(current_time.second, current_time.microsecond)
        return (hour_hand_index, minute_hand_index, second_hand_index)

    def __insert(self, indices):
        for rainy_index in self.__rainy_indices:
            self.__indices_to_address.insert(rainy_index, Diode(rainy_index, self.service.colors_controller.rain_color))
        colors_to_use = (self.service.colors_controller.hour_hand_color, self.service.colors_controller.minute_hand_color, self.service.colors_controller.second_hand_color)
        for index in range(len(indices)):
            if self.current_indices[index] != indices[index] and self.current_indices[index] not in self.__rainy_indices:
                self.__turn_off(self.current_indices[index])
            self.current_indices[index] = indices[index]
            diode = self.__indices_to_address.get(indices[index])
            color = colors_to_use[index]
            if diode:
                color = Color.mix([diode.color, color])
                diode.color = color
                self.__indices_to_address[indices[index]] = diode
            else:
                self.__indices_to_address[indices[index]] = Diode(indices[index], colors_to_use[index])

    def __turn_off(self, index_to_turn_off):
        self.service.led_event_handler.turn_off_diode(index_to_turn_off)


    # Weather Data provided by the weather-data-controller will be requested. This weather data containing entries
    # for each minute which has more than a 60 percent probability of precipitation. The minute is stored on the first index of the data object.
    # The specific minute will be than displayed in a light blue color. Further more because a minute representation within the clock can be more than only
    # one led-diode. The relative section which represents one minute will be calculated and also illuuminated.
    def __update_weather_data(self, weather_data):
        self.__rainy_indices.clear()
        diodes_per_one_minute = self.service.led_count / 60
        for data in weather_data:
            start = int(data[0] * diodes_per_one_minute)
            end = int(start + diodes_per_one_minute)
            self.__rainy_indices.extend(range(start, end))


    def react_on_motion(self):
        self.__switch_to_state_function(StateType.sundial_state)

    def clear(self):
        self.service.weather_data_controller.log_off_minutely_listener(self.__register_for_weather_data_function)
