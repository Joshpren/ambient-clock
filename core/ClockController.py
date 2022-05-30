import threading
import time

from core.ArithmeticLogicUnit import ArithmeticLogicUnit
from core.ClockPrinter import ClockPrinter
from entities.Diode import Diode
from fsm.AmbientState import AmbientState
from fsm.Conext import Context
from fsm.ErrorState import ErrorState
from fsm.OrdinalState import OrdinalState
from fsm.StateType import StateType
from fsm.SundialState import SundialState


class ClockController:

    def __init__(self, number_of_leds, position_of_start, color_controller):
        self.__number_of_leds = number_of_leds
        self.__alu = ArithmeticLogicUnit(number_of_leds, position_of_start)
        self.__color_controller = color_controller
        self.__state = OrdinalState(lambda hand_indexes : self.address_led(hand_indexes), lambda: self.show_hands() ,lambda new_state : self.switch_to_state(new_state))
        self.__sleep = float(60/number_of_leds)
        self.diodes_to_show = []

    def address_led(self, diode):
        self.diodes_to_show.append(diode)

    def show_diodes(self):
        print (self.diodes_to_show)
        self.diodes_to_show.clear()

    def show_hands(self):
        ClockPrinter(self.__alu).printClock(self.diodes_to_show[0], self.diodes_to_show[1], self.diodes_to_show[2])
        time.sleep(0.2)
        self.diodes_to_show.clear()

    def switch_to_state(self, new_state):
        self.__state.running(False)
        if new_state == StateType.ordinal_state:
            self.__state = OrdinalState(lambda diode : self.address_led(diode), lambda: self.show_hands(), lambda new_state : self.switch_to_state(new_state))
        elif new_state == StateType.sundial_state:
            self.__state = SundialState(lambda diode : self.address_led(diode), lambda: self.show_hands(), lambda new_state : self.switch_to_state(new_state))
        elif new_state == StateType.ambient_state:
            self.__state = AmbientState(lambda diode: self.address_led(diode), lambda: self.show_diodes(), lambda new_state: self.switch_to_state(new_state))

    def react_on_motion(self):
        self.__state = ErrorState(lambda diode: self.address_led(diode), lambda: self.show_diodes(), None)

    def start_state(self):
        try:
            self.__state.start(Context(self.__alu, self.__color_controller, self.__number_of_leds))
        except Exception as e:
            print(e.with_traceback())
            self.__state = ErrorState(lambda diode: self.address_leds_with_single_diode(diode), None)

    def start(self):
        print("Start")
        print(threading.get_native_id())
        while True:
            self.start_state()