from core.ClockPrinter import ClockPrinter
from entities.Color import Color
from entities.Diode import Diode


class LedStrip:


    def __init__(self, led_count):
        self.__led_count = led_count
        self.__active_diodes = []
        temp = []
        for index in range(led_count):
            temp.append(Color(0, 0, 0))
        self.__strip = temp

    @property
    def led_count(self) -> int:
        return self.__led_count

    def address_diode(self, diode):
        index = diode.index
        self.__strip[index] = diode.color
        self.__active_diodes.append(index)

    def address_diodes(self, diodes):
        for diode in diodes:
            self.address_diode(diode)

    def turn_off_diode(self, index):
        self.__strip[index] = Color(0, 0, 0)

    def clear_strip(self):
        for index in self.__active_diodes:
            self.turn_off_diode(index)
        self.__active_diodes.clear()


    def show(self):
        print(self.__strip)

    def show_hands(self):
        ClockPrinter(self.__service.arithmetic_logic_unit).printClock(self.diodes_to_show[0], self.diodes_to_show[1], self.diodes_to_show[2], self.diodes_to_show[3:len(self.diodes_to_show)])