import datetime
import time
from abc import ABC
from entities.Hand import Hand

from fsm.State import State
from fsm.StateType import StateType


class SundialState(State, ABC):
    pass

    def __init__(self, alu, address_led_function, switch_to_state_function):
        self.alu = alu
        self.__address_led_function = address_led_function
        self.__switch_to_state_function = switch_to_state_function
        self.__hour_hand = Hand()
        self.__minute_hand = Hand()
        self.__second_hand = Hand()

    def address_leds(self):
        self.set_time()
        self.switchBy180Degrees()
        self.__address_led_function(self.__hour_hand, self.__minute_hand, self.__second_hand)
        time.sleep(0.5)

    def prev_state(self):
        return self.__prev_state

    def react_on_motion(self):
        print("Sundial State Switch")
        self.running(False)
        self.__switch_to_state_function(StateType.ordinal_state)

    def set_time(self):
        current_time = datetime.datetime.now()
        self.__hour_hand.index = self.alu.determine_index_by_hours(current_time.hour, current_time.minute)
        self.__minute_hand.index = self.alu.determine_index_by_minutes(current_time.minute, current_time.second)
        self.__second_hand.index = self.alu.determine_index_by_seconds(current_time.second, current_time.microsecond)

    def switchBy180Degrees(self):
        new_index_for_hour_hand = self.alu.switchBy180Degrees(self.__hour_hand.index)
        new_index_for_minute_hand = self.alu.switchBy180Degrees(self.__minute_hand.index)
        new_index_for_second_hand = self.alu.switchBy180Degrees(self.__second_hand.index)
        self.__hour_hand.index = new_index_for_hour_hand
        self.__minute_hand.index = new_index_for_minute_hand
        self.__second_hand.index = new_index_for_second_hand