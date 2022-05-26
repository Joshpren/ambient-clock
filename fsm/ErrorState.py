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
        self.__colors = [Color(255,0,0)]

    def address_leds(self):
        for index in range(120):
            self.__address_led_function(Diode(index, self.__colors[0]))
        self.__show_function()
        time.sleep(2)

    def react_on_motion(self):
        print("Error")

