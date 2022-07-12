import threading
from math import ceil, floor

from controller.LedEventHandler import LedEventHandler
from controller.TransmissionController import TransmissionController
from controller.WeatherDataController import WeatherDataController
from controller.ClockController import ClockController
from controller.ColorsController import ColorController
from core.ArithmeticLogicUnit import ArithmeticLogicUnit
from core.ServiceProvider import ServiceProvider
from entities.Color import Color
from entities.LedStrip import LedStrip
from fsm.StateType import StateType


class Launcher:

    @classmethod
    def userInput(cls, clock_controller, color_controller):
        try:
            while True:
                userInput = input()
                if userInput == "q":
                    running = False
                    print("Exit")
                elif userInput == "1":
                    clock_controller.react_on_motion()
                elif userInput == "e":
                    color_controller.hour_hand_color = Color.random()
                elif userInput == "a":
                    clock_controller.switch_to_state(StateType.ambient_state)
                elif userInput == "w":
                    clock_controller.switch_to_state(StateType.weather_state)
                elif userInput == "o":
                    clock_controller.switch_to_state(StateType.ordinal_state)
                elif userInput == "t":
                    if clock_controller.service.transmission_controller:
                        clock_controller.service.transmission_controller = None
                    else:
                        clock_controller.service.transmission_controller = TransmissionController(clock_controller.service.led_count)
        except KeyboardInterrupt:
            pass


    def init(cls):
        led_count, offset = int(input("Wie viele LEDs werden verwendet")), int(input("Versatz?"))
        color_controller = ColorController.init()
        weather_data_controller = WeatherDataController.init()
        arithmetic_logic_unit = ArithmeticLogicUnit(led_count, offset)
        led_strip = LedStrip(led_count)
        led_event_handler = LedEventHandler(led_strip)
        service = ServiceProvider(arithmetic_logic_unit, color_controller, weather_data_controller, led_event_handler)
        return ClockController.init(service), color_controller


controller, color_controller = Launcher.init(Launcher)
controller.start()
Launcher.userInput(controller, color_controller)

SystemExit
