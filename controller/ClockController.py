from __future__ import annotations
import logging
import threading
import traceback
from threading import Event
from controller.AbstractController import AbstractController
from core.EventLoop import EventLoop
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
        self.__running_event = None
        self.__current_state = AnalogState(lambda new_state : self.switch_to_state(new_state))

    @property
    def service(self) -> ServiceProvider:
        return self.__service

    def switch_to_state(self, new_state):
        self.__running_event.stop(lambda *args: self.__current_state.clear())
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
        self.__start_state(state)

    def react_on_motion(self):
        self.__current_state.react_on_motion()

    def __start_state(self, state):
        state.init(self.__service)
        self.__running_event = EventLoop(lambda *args: state.run())
        try:
            self.__current_state = state
            self.__running_event.run()
        except:
            print(traceback.format_exc())
            error_state = ErrorState(None)
            error_state.init(self.__service)
            self.__current_state = error_state


    def start(self):
        logging.warning("Controller has been started")
        self.__start_state(self.__current_state)

    @classmethod
    def init(cls, service) -> ClockController:
        controller = ClockController(service)
        return controller