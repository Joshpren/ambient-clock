from __future__ import annotations

from controller import TransmissionController, LedEventHandler
from controller.ColorsController import ColorController
from controller.WeatherDataController import WeatherDataController
from core import ArithmeticLogicUnit


class ServiceProvider:

    def __init__(self, alu, colors_controller, weather_data_controller, led_event_handler):
        self.__arithmetic_logic_unit = alu
        self.__colors_controller = colors_controller
        self.__weather_data_controller = weather_data_controller
        self.__led_event_handler = led_event_handler
        self.__transmission_controller = None

    @property
    def led_event_handler(self) -> LedEventHandler:
        return self.__led_event_handler

    @property
    def transmission_controller(self) -> TransmissionController:
        return self.__transmission_controller

    @transmission_controller.setter
    def transmission_controller(self, new_transmission_controller):
        self.__transmission_controller = new_transmission_controller

    @property
    def led_count(self) -> int:
        return self.__led_event_handler.led_count

    @property
    def arithmetic_logic_unit(self) -> ArithmeticLogicUnit:
        return self.__arithmetic_logic_unit

    @property
    def colors_controller(self) -> ColorController:
        return self.__colors_controller

    @property
    def weather_data_controller(self) -> WeatherDataController:
        return self.__weather_data_controller

    @classmethod
    def init(cls, arithmetic_logic_unit, colors_controller, weather_data_controller, led_event_handler):
        return ServiceProvider(arithmetic_logic_unit, colors_controller, weather_data_controller, led_event_handler)
