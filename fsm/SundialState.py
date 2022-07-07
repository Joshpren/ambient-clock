import datetime
import logging
import time
from abc import ABC

from entities.Color import Color
from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class SundialState(State, ABC):
    pass

    current_indices = [0, 0, 0]

    def __init__(self, switch_to_state_function):
        self.__switch_to_state_function = switch_to_state_function
        self.__indices_to_address = {}

    def start(self):
        logging.info("SunDial-State has been started!")

    def address_leds(self):
        current_time = datetime.datetime.now()
        self.__insert(self.determine_indices(current_time))
        for diode in self.__indices_to_address.values():
            self.service.led_event_handler.address_diode(diode)
        self.service.led_event_handler.show()
        self.__indices_to_address.clear()
        time.sleep(0.5)


    def determine_indices(self, current_time):
        hour_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_hours(current_time.hour, current_time.minute)
        minute_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_minutes(current_time.minute, current_time.second)
        second_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_seconds(current_time.second, current_time.microsecond)
        return [hour_index, minute_index, second_index]

    def __insert(self, indices):
        colors_to_use = (self.service.colors_controller.hour_hand_color, self.service.colors_controller.minute_hand_color, self.service.colors_controller.second_hand_color)
        for index in range(len(indices)):
            if self.current_indices[index] not in indices:
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

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.ordinal_state)

    def clear(self):
        logging.info("SunDial-State has been cleared")
