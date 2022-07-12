import datetime
import logging
import time
from abc import ABC
from entities.Color import Color
from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class StandbyState(State, ABC):
    pass

    def __init__(self, switch_to_state_function):
        self.__switch_to_state_function = switch_to_state_function

    def start(self):
        logging.info("Standby-State has been started!")
        print("Standby-State has been started!")
        self.service.led_event_handler.clear_strip().show()

    def run(self):
        self.address_leds()

    def address_leds(self):
        pass

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.sundial_state)

    def clear(self):
        logging.info("Standbye-State has been cleared")
