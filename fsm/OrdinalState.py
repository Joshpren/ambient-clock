import time
import datetime
from abc import ABC

from entities.Hand import Hand
from fsm.State import State
from fsm.StateType import StateType


class OrdinalState(State, ABC):
    pass

    def __init__(self, alu, address_led_function, switch_to_state_function):
        self.alu = alu
        self.__address_led_function = address_led_function
        self.__switch_to_state_function = switch_to_state_function
        self.__hour_hand = Hand()
        self.__minute_hand = Hand()
        self.__second_hand = Hand()


        @property
        def hour_hand(self):
            return self.__hour_hand

        @property
        def minute_hand(self):
            return self.__minute_hand

        @property
        def second_hand(self):
            return self.__second_hand


    def address_leds(self):
        self.set_time()
        self.__address_led_function(self.__hour_hand, self.__minute_hand, self.__second_hand)
        time.sleep(0.5)

    def set_time(self):
        current_time = datetime.datetime.now()
        self.__hour_hand.index = self.alu.determine_index_by_hours(current_time.hour, current_time.minute)
        self.__minute_hand.index = self.alu.determine_index_by_minutes(current_time.minute, current_time.second)
        self.__second_hand.index = self.alu.determine_index_by_seconds(current_time.second, current_time.microsecond)

    def react_on_motion(self):
        self.__switch_to_state_function(StateType.sundial_state)