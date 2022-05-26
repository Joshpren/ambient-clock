import time
from abc import ABC
from entities.Color import Color
from entities.Diode import Diode
from fsm.StateType import StateType
from fsm.State import State


class AmbientState(State, ABC):
    pass

    def __init__(self, address_led_function, show_diodes_function, switch_to_state_function, number_of_led):
        self.__address_led_function = address_led_function
        self.__show_diodes_function = show_diodes_function
        self.__switch_to_state_function = switch_to_state_function
        self.__number_of_led = number_of_led

    def address_leds(self):
        self.color_wipe()

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.sundial_state)

    def color_wipe(self):
        color = Color.random()
        for index in range(self.__number_of_led):
            self.__address_led_function(Diode(index, color))
            self.__show_diodes_function()
            time.sleep(0.2)

    #def rainbow(self):
     #for j in range(256):
      #      for index in range(120):
       #         self.__address_led_function(Diode(index, Color(wheel((index + j) & 255))
        #    self.__show_diodes_function()
         #   time.sleep(20 / 1000.0)