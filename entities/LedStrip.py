from core.ClockPrinter import ClockPrinter
from entities.Color import Color
from entities.Diode import Diode


class LedStrip:


    def __init__(self, led_count):
        self.__led_count = led_count
        temp = []
        for index in range(led_count):
            temp.append(Color(0, 0, 0))
        self.__strip = temp

    @property
    def led_count(self) -> int:
        return self.__led_count

    def address_diode(self, diode):
        self.__strip[diode.index] = diode.color

    def turn_off_diode(self, index):
        self.__strip[index] = Color(0, 0, 0)

    def show(self):
        print(self.__strip)

    def show_hands(self):
        ClockPrinter(self.__service.arithmetic_logic_unit).printClock(self.diodes_to_show[0], self.diodes_to_show[1], self.diodes_to_show[2], self.diodes_to_show[3:len(self.diodes_to_show)])