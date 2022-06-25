from __future__ import annotations
import logging
import threading
from controller.AbstractController import AbstractController
from core.ArithmeticLogicUnit import ArithmeticLogicUnit
from core.ClockPrinter import ClockPrinter
from fsm.AmbientState import AmbientState
from core.ServiceProvider import ServiceProvider
from fsm.ErrorState import ErrorState
from fsm.OrdinalState import OrdinalState
from fsm.StateType import StateType
from fsm.SundialState import SundialState
from fsm.WeatherState import WeatherState

class ClockController(AbstractController):

    def __init__(self, number_of_leds, position_of_start, color_controller, weather_data_controller):
        self.__service = ServiceProvider(ArithmeticLogicUnit(number_of_leds, position_of_start), color_controller, weather_data_controller, number_of_leds)
        self.__current_state = OrdinalState(lambda diode : self.address_led(diode), lambda: self.show_hands(), lambda index : self.clear_diode(index), lambda new_state : self.switch_to_state(new_state))
        self.diodes_to_show = []

    def address_led(self, diode):
        self.diodes_to_show.append(diode)

    def show_diodes(self):
        print (self.diodes_to_show)
        self.diodes_to_show.clear()

    def show_hands(self):
        ClockPrinter(self.__service.arithmetic_logic_unit).printClock(self.diodes_to_show[0], self.diodes_to_show[1], self.diodes_to_show[2], self.diodes_to_show[3:len(self.diodes_to_show)])
        self.diodes_to_show.clear()

    def clear_diode(self, index):
        self.diodes_to_show.pop(index)

    def switch_to_state(self, new_state):
        self.__current_state.clear()
        state = None
        if new_state == StateType.ordinal_state:
            state = OrdinalState(lambda diode : self.address_led(diode), lambda: self.show_hands(), lambda index : self.clear_diode(index), lambda new_state : self.switch_to_state(new_state))
        elif new_state == StateType.sundial_state:
            state = SundialState(lambda diode : self.address_led(diode), lambda: self.show_hands(), lambda new_state : self.switch_to_state(new_state))
        elif new_state == StateType.ambient_state:
            state = AmbientState(lambda diode: self.address_led(diode), lambda: self.show_diodes(), lambda new_state: self.switch_to_state(new_state))
        elif new_state == StateType.weather_state:
            state = WeatherState(lambda diode: self.address_led(diode), lambda: self.show_diodes(), lambda new_state: self.switch_to_state(new_state))
        else:
            state = ErrorState(lambda diode: self.address_leds_with_single_diode(diode), None)
        state.init(self.__service)
        self.__current_state = state

    def react_on_motion(self):
        self.__current_state.react_on_motion()


    def start(self):
        logging.warning("Controller has been started")
        print(threading.get_native_id())
        self.__current_state.init(self.__service)
        while True:
            try:
                self.__current_state.address_leds()
            except:
                self.__current_state = ErrorState(lambda diode: self.address_leds_with_single_diode(diode), None)

    @classmethod
    def init(cls, number_of_leds, position_of_start, color_controller, weather_data_controller) -> ClockController:
        controller = ClockController(number_of_leds, position_of_start, color_controller, weather_data_controller)
        return controller