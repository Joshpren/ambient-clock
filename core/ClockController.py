import threading
import time

from core.ArithmeticLogicUnit import ArithmeticLogicUnit
from core.ClockPrinter import ClockPrinter
from entities.Diode import Diode
from fsm.AmbientState import AmbientState
from fsm.ErrorState import ErrorState
from fsm.OrdinalState import OrdinalState
from fsm.StateType import StateType
from fsm.SundialState import SundialState


class ClockController:

    def __init__(self, number_of_leds, position_of_start, color_controller):
        self.__number_of_leds = number_of_leds
        self.__alu = ArithmeticLogicUnit(number_of_leds, position_of_start)
        self.__color_controller = color_controller
        self.__state = OrdinalState(self.__alu, lambda hand_indexes : self.address_led_with_hands(hand_indexes), lambda: self.show_hands() ,lambda new_state : self.switch_to_state(new_state))
        self.__sleep = float(60/number_of_leds)
        self.diodes_to_show = []


    def address_leds_with_single_diode(self, diode):
        if(len(self.diodes_to_show) == 12):
            self.diodes_to_show[diode.index] = diode
        else:
            self.diodes_to_show.insert(diode.index, diode)

    def address_leds_with_index(self, index):
        self.diodes_to_show.insert(Diode(index))


    def show_diodes(self):
        print(threading.get_native_id())
        print (self.diodes_to_show)

    #first = hour-index
    #second = minute-index
    #third = second-index
    def address_led_with_hands(self, hand_indexes):
        self.diodes_to_show.insert(0, Diode(hand_indexes[0], self.__color_controller.hour_hand_color))
        self.diodes_to_show.insert(1, Diode(hand_indexes[1], self.__color_controller.minute_hand_color))
        self.diodes_to_show.insert(2, Diode(hand_indexes[2], self.__color_controller.second_hand_color))

    def show_hands(self):
        ClockPrinter(self.__alu).printClock(self.diodes_to_show[0], self.diodes_to_show[1], self.diodes_to_show[2])
        time.sleep(self.__sleep)
        self.diodes_to_show.clear()

    def switch_to_state(self, new_state):
        self.__state.running(False)
        if new_state == StateType.ordinal_state:
            self.__state = OrdinalState(self.__alu, lambda hand_indexes : self.address_led_with_hands(hand_indexes), lambda: self.show_hands() ,lambda new_state : self.switch_to_state(new_state))
        elif new_state == StateType.sundial_state:
            self.__state = SundialState(self.__alu, lambda hand_indexes : self.address_led_with_hands(hand_indexes), lambda: self.show_hands() ,lambda new_state : self.switch_to_state(new_state))
        elif new_state == StateType.ambient_state:
            self.__state = AmbientState(lambda diode: self.address_leds_with_single_diode(diode), lambda: self.show_diodes(), lambda new_state: self.switch_to_state(new_state), self.__number_of_leds)

    def react_on_motion(self):
        self.__state.react_on_motion()

    def start_state(self):
        try:
            self.__state.start()
        except Exception as e:
            print(e.with_traceback())
            self.__state = ErrorState(lambda diode: self.address_leds_with_single_diode(diode), None)

    def start(self):
        print("Start")
        while True:
            self.start_state()