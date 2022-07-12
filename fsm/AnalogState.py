import datetime
import time
from abc import ABC
from timeit import default_timer as timer
from controller.TransmissionController import TransmissionController
from effects.Carousel import CarouselEffect
from entities.Color import Color
from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class AnalogState(State, ABC):
    pass

    def __init__(self, switch_to_state_function):
        self.__switch_to_state_function = switch_to_state_function
        self.__register_for_weather_data_function = lambda data: self.__update_weather_data(data)
        self.__display_rainy_minutes = True
        self.__rainy_indices = []

    def start(self):
        if self.__display_rainy_minutes == True:
            self.service.weather_data_controller.register_minutely_listener(self.__register_for_weather_data_function)

    def run(self):
        self.address_leds()

    def address_leds(self):
        self.service.led_event_handler.clear_strip()
        current_time = datetime.datetime.now()
        indices_to_address = self.__determine_indices_to_address(current_time)
        self.service.led_event_handler.address_diodes(indices_to_address.values())
        self.service.led_event_handler.show()
        time.sleep(0.1)

    def __determine_time_diodes(self, current_time):
        hour_hand_index = self.service.arithmetic_logic_unit.determine_index_by_hours(current_time.hour, current_time.minute)
        minute_hand_index = self.service.arithmetic_logic_unit.determine_index_by_minutes(current_time.minute, current_time.second)
        second_hand_index = self.service.arithmetic_logic_unit.determine_index_by_seconds(current_time.second, current_time.microsecond)
        diodes = self.__indices_to_diodes([hour_hand_index, minute_hand_index, second_hand_index], current_time)
        return diodes

    def __indices_to_diodes(self, indices, current_time):
        diodes = []
        orders = ("hour", "minute", "second")
        colors_to_use = (self.service.colors_controller.hour_hand_color, self.service.colors_controller.minute_hand_color, self.service.colors_controller.second_hand_color)
        for index in range(len(indices)):
            order = orders[index]
            color = colors_to_use[index]
            diode_index = indices[index]
            if self.service.transmission_controller:
                    darkening, brightnening = self.service.transmission_controller.transmission(order, current_time)
                    diodes.append(Diode(diode_index, Color.copy(color, darkening*color.brightness)))
                    diodes.append(Diode((diode_index + 1)%self.service.led_count, Color.copy(color, brightnening*color.brightness)))
            else:
                diodes.append(Diode(diode_index, color))
        return diodes

    def __determine_indices_to_address(self, current_time):
        indices_to_address = {}
        time_diodes_to_address = self.__determine_time_diodes(current_time)
        for rainy_index in self.__rainy_indices:
            indices_to_address[rainy_index] = Diode(rainy_index, self.service.colors_controller.rain_color)
        for time_diode in time_diodes_to_address:
            diode = indices_to_address.get(time_diode.index)
            if diode:
                color = Color.mix([diode.color, time_diode.color])
                diode.color = color
                indices_to_address[time_diode.index] = diode
            else:
                indices_to_address[time_diode.index] = time_diode
        return indices_to_address


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
        CarouselEffect(self.service.led_event_handler, self.service.colors_controller).build_up()

