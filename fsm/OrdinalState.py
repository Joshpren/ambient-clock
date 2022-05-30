import datetime
from abc import ABC

from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class OrdinalState(State, ABC):
    pass

    def __init__(self, address_led_function, show_hands_function, switch_to_state_function):
        self.__address_led_function = address_led_function
        self.__show_hands_function = show_hands_function
        self.__switch_to_state_function = switch_to_state_function

    def address_leds(self):
        current_time = datetime.datetime.now()
        indices = self.determine_indices(current_time)
        self.__address_led_function(Diode(indices[0], self.context.colors_controller.hour_hand_color))
        self.__address_led_function(Diode(indices[1], self.context.colors_controller.minute_hand_color))
        self.__address_led_function(Diode(indices[2], self.context.colors_controller.second_hand_color))
        self.__show_hands_function()

    def determine_indices(self, current_time):
        hour_index = self.context.arithmetic_logic_unit.determine_index_by_hours(current_time.hour, current_time.minute)
        minute_index = self.context.arithmetic_logic_unit.determine_index_by_minutes(current_time.minute, current_time.second)
        second_index = self.context.arithmetic_logic_unit.determine_index_by_seconds(current_time.second, current_time.microsecond)
        return [hour_index, minute_index, second_index]

    def react_on_motion(self):
        self.__switch_to_state_function(StateType.sundial_state)