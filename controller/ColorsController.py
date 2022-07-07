from __future__ import annotations
from controller.AbstractController import AbstractController
from entities.Color import Color

class ColorController(AbstractController):

    def __init__(self):
        self.__colors_to_use = []
        self.__hour_hand_color = Color.white(0.7)
        self.__minute_hand_color = Color.white(0.8)
        self.__second_hand_color = Color.white(0.9)
        self.__rain_color = Color(65, 178, 240)

    @property
    def colors_to_use(self):
        if len(self.__colors_to_use) == 0:
            return [Color.random() * 4]
        else:
            return self.__colors_to_use

    @colors_to_use.setter
    def colors_to_use(self, new_colors_to_use):
        self.__colors_to_use = new_colors_to_use

    @property
    def rain_color(self):
        return self.__rain_color

    @rain_color.setter
    def rain_color(self, new_rain_color):
        self.__rain_color = new_rain_color

    def red(self, brightness):
        color = Color(255, 0, 0)
        color.brightness = brightness
        return color

    def green(self, brightness):
        color = Color(0, 255, 0)
        color.brightness = brightness
        return color

    def blue(self, brightness):
        color = Color(0, 0, 255)
        color.brightness = brightness
        return color

    def random(self):
        return Color.random()

    @property
    def hour_hand_color(self):
        return self.__hour_hand_color

    @hour_hand_color.setter
    def hour_hand_color(self, new_color):
        self.__hour_hand_color = new_color

    @property
    def minute_hand_color(self):
        return self.__minute_hand_color

    @minute_hand_color.setter
    def minute_hand_color(self, new_color):
         self.__minute_hand_color = new_color

    @property
    def second_hand_color(self):
        return self.__second_hand_color

    @second_hand_color.setter
    def second_hand_color(self, new_color):
        self.__second_hand_color = new_color

    def start(self):
        #do nothing
        print()

    @classmethod
    def init(cls) -> ColorController:
        return ColorController()