import datetime
import logging
import time
from abc import ABC

from controller.TransmissionController import TransmissionController
from entities.Color import Color
from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class SundialState(State, ABC):
    pass

    def __init__(self, switch_to_state_function):
        self.__switch_to_state_function = switch_to_state_function
        self.__transmission_controller = None


    @property
    def transmission_controller(self):
        return self.__transmission_controller

    @transmission_controller.setter
    def transmission_controller(self, transmission_controller):
        self.__transmission_controller = transmission_controller

    def start(self):
        logging.info("SunDial-State has been started!")
        print("SunDial-State has been started!")
        self.__transmission_controller = TransmissionController(self.service.led_count)

    def address_leds(self):
        current_time = datetime.datetime.now()
        indices_to_address = self.__determine_indices_to_address(current_time)
        self.service.led_event_handler.address_diodes(indices_to_address.values())
        self.service.led_event_handler.show()
        self.service.led_event_handler.clear_strip()
        time.sleep(0.1)

    def __determine_time_diodes(self, current_time):
        hour_hand_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_hours(current_time.hour, current_time.minute)
        minute_hand_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_minutes(current_time.minute, current_time.second)
        second_hand_index = self.service.arithmetic_logic_unit.determine_sundial_index_by_seconds(current_time.second, current_time.microsecond)
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
            if self.__transmission_controller:
                darkening, brightnening = self.__transmission_controller.transmission(order, current_time)
                diodes.append(Diode(diode_index, Color.copy(color, darkening * color.brightness)))
                diodes.append(Diode((diode_index + 1) % self.service.led_count,
                                    Color.copy(color, brightnening * color.brightness)))
            else:
                diodes.append(Diode(diode_index, color))
        return diodes

    def __determine_indices_to_address(self, current_time):
        indices_to_address = {}
        time_diodes_to_address = self.__determine_time_diodes(current_time)
        for time_diode in time_diodes_to_address:
            diode = indices_to_address.get(time_diode.index)
            if diode:
                color = Color.mix([diode.color, time_diode.color])
                diode.color = color
                indices_to_address[time_diode.index] = diode
            else:
                indices_to_address[time_diode.index] = time_diode
        return indices_to_address

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.ordinal_state)

    def clear(self):
        logging.info("SunDial-State has been cleared")
