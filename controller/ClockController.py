from __future__ import annotations
import logging
import threading
import traceback

from controller.AbstractController import AbstractController
from core.ServiceProvider import ServiceProvider
from fsm.AmbientState import AmbientState
from fsm.ErrorState import ErrorState
from fsm.AnalogState import AnalogState
from fsm.StateType import StateType
from fsm.SundialState import SundialState
from fsm.WeatherState import WeatherState

class ClockController(AbstractController):

    def __init__(self,  service):
        self.__service = service
        self.__current_state = AnalogState(lambda new_state : self.switch_to_state(new_state))

    @property
    def service(self) -> ServiceProvider:
        return self.__service

    def switch_to_state(self, new_state):
        self.__current_state.clear()
        state = None
        if new_state == StateType.ordinal_state:
            state = AnalogState(lambda new_state : self.switch_to_state(new_state))
        elif new_state == StateType.sundial_state:
            state = SundialState(lambda new_state : self.switch_to_state(new_state))
        elif new_state == StateType.ambient_state:
            state = AmbientState(lambda new_state: self.switch_to_state(new_state))
        elif new_state == StateType.weather_state:
            state = WeatherState(lambda new_state: self.switch_to_state(new_state))
        else:
            state = ErrorState(None)
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
                print(traceback.format_exc())
                error_state = ErrorState(None)
                error_state.init(self.__service)
                self.__current_state = error_state

    @classmethod
    def init(cls, service) -> ClockController:
        controller = ClockController(service)
        return controller