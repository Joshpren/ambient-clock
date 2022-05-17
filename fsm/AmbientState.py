import time
from abc import ABC

from fsm.StateType import StateType
from fsm.State import State


class AmbientState(State, ABC):
    pass

    def __init__(self, address_led_function, switch_to_state_function):
        self.__address_led_function = address_led_function
        self.__switch_to_state_function = switch_to_state_function

    def address_leds(self):
        indices = list(range(1, 120))
        self.__address_led_function(indices)
        time.sleep(2)

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.sundial_state)
