from core.ArithmeticLogicUnit import ArithmeticLogicUnit
from core.ClockPrinter import ClockPrinter
from entities.Diode import Diode
from fsm.AmbientState import AmbientState
from fsm.ErrorState import ErrorState
from fsm.OrdinalState import OrdinalState
from fsm.StateType import StateType
from fsm.SundialState import SundialState


class ClockController:

    def __init__(self, number_of_leds, position_of_start, hour_hand, minute_hand, second_hand):
        self.__number_of_leds = number_of_leds
        self.__hour_hand = hour_hand
        self.__minute_hand = minute_hand
        self.__second_hand = second_hand
        self.__alu = ArithmeticLogicUnit(number_of_leds, position_of_start)
        self.__state = OrdinalState(self.__alu, lambda hour_hand, minute_hand, second_hand : self.address_led_with_hands(hour_hand, minute_hand, second_hand),lambda new_state : self.switch_to_state(new_state))

    def address_leds_with_indices(self, indices):
        print(indices)
        #yet to come

    def address_led_with_hands(self, hour_hand, minute_hand, second_hand):
        ClockPrinter(self.__alu).printClock(hour_hand.index, minute_hand.index, second_hand.index)




    def switch_to_state(self, new_state):
        try:
            self.__state.running(False)
            if new_state == StateType.ordinal_state:
                self.__state = OrdinalState(self.__alu, lambda hour_hand, minute_hand, second_hand : self.address_led_with_hands(hour_hand, minute_hand, second_hand),lambda new_state : self.switch_to_state(new_state))
            elif new_state == StateType.sundial_state:
                self.__state = SundialState(self.__alu, lambda hour_hand, minute_hand, second_hand : self.address_led_with_hands(hour_hand, minute_hand, second_hand),lambda new_state : self.switch_to_state(new_state))
            elif new_state == StateType.ambient_state:
                self.__state = AmbientState(lambda indices: self.address_leds_with_indices(indices), lambda new_state: self.switch_to_state(new_state))
        except:
            self.__state = ErrorState(lambda indices: self.address_leds_with_indices(indices), None)
        self.start_state()

    def react_on_motion(self):
        self.__state.react_on_motion()

    def start(self):
        print("start")
        while True:
            self.start_state()


    def start_state(self):
        self.__state.start()