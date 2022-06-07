from __future__ import annotations
from controller.ColorsController import ColorController
from controller.WeatherDataController import WeatherDataController
from core import ArithmeticLogicUnit


class ServiceProvider:

    def __init__(self, alu, colors_controller, weather_data_controller, number_of_led):
        self.__arithmetic_logic_unit = alu
        self.__colors_controller = colors_controller
        self.__weather_data_controller = weather_data_controller
        self.__number_of_led = number_of_led

    @property
    def number_of_led(self):
        return self.__number_of_led

    @property
    def arithmetic_logic_unit(self) -> ArithmeticLogicUnit:
        return self.__arithmetic_logic_unit

    @property
    def colors_controller(self) -> ColorController:
        return self.__colors_controller

    @property
    def weather_data_controller(self) -> WeatherDataController:
        return self.__weather_data_controller