import time
from abc import ABC
from effects.Effect import Effect
from entities.Color import Color
from entities.Diode import Diode

class CarouselEffect(Effect, ABC):
    pass

    def __init__(self, led_event_handler, colors_controller):
        self.__led_event_handler = led_event_handler
        self.__colors_controller = colors_controller

    def build_up(self):
        color_to_use = self.__colors_controller.colors_to_use[0]
        for index in range(self.__led_event_handler.led_count):
            self.__led_event_handler.address_diode(Diode(index, color_to_use)).show()
            time.sleep(0.1)

    def build_down(self):
        for index in reversed(range(self.__led_event_handler.led_count)):
            self.__led_event_handler.address_diode(Diode(index, Color(0,0,0))).show()
            time.sleep(0.1)