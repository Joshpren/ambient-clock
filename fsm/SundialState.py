import datetime
import logging
import time
from abc import ABC
from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class SundialState(State, ABC):
    pass

    def __init__(self, address_led_function, show_hands_function, switch_to_state_function):
        self.__address_led_function = address_led_function
        self.__show_hands_function = show_hands_function
        self.__switch_to_state_function = switch_to_state_function

    def start(self):
        logging.info("SunDial-State has been started!")

    def address_leds(self):
        current_time = datetime.datetime.now()
        indices = self.determine_indices(current_time)
        self.__address_led_function(Diode(indices[0], self.service.colors_controller.hour_hand_color))
        self.__address_led_function(Diode(indices[1], self.service.colors_controller.minute_hand_color))
        self.__address_led_function(Diode(indices[2], self.service.colors_controller.second_hand_color))
        self.__show_hands_function()
        time.sleep(0.5)


    def determine_indices(self, current_time):
        hour_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_hours(current_time.hour, current_time.minute)
        minute_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_minutes(current_time.minute, current_time.second)
        second_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_seconds(current_time.second, current_time.microsecond)
        return [hour_index, minute_index, second_index]

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.ordinal_state)

    def clear(self):
        logging.info("SunDial-State has been cleared")
