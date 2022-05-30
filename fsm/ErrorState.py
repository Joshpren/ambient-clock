import time
from abc import ABC

from entities.Color import Color
from entities.Diode import Diode
from fsm.State import State


class ErrorState(State, ABC):
    pass

    def __init__(self, address_led_function, show_function, switch_to_state_function):
        self.__address_led_function = address_led_function
        self.__show_function = show_function
        self.__switch_to_state_function = switch_to_state_function

    def address_leds(self):
        for brightness in range(255):
            for index in range(self.context.number_of_led):
                self.__address_led_function(Diode(index, self.context.colors_controller.red(brightness)))
            self.__show_function()
        for brightness in range(255, -1, -1):
            for index in range(self.context.number_of_led):
                self.__address_led_function(Diode(index, self.context.colors_controller.red(brightness)))
            self.__show_function()

    def react_on_motion(self):
        print("Error")

