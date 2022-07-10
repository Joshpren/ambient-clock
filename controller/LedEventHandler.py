from core.ClockPrinter import ClockPrinter


class LedEventHandler:

    def __init__(self, led_strip):
        self.__led_strip = led_strip

    @property
    def led_count(self) -> int:
        return self.__led_strip.led_count

    def address_diode(self, diode):
        color = diode.color
        self.__led_strip.address_diode(diode.index, color.red, color.green, color.blue)
        return self

    def address_diodes(self, diodes):
        for diode in diodes:
            self.__led_strip.address_diode(diodes)
        return self

    def turn_off_diode(self, index):
        self.__led_strip.turn_off_diode(index)
        return self

    def clear_strip(self):
        self.__led_strip.clear_strip()
        return self

    def show(self):
        self.__led_strip.show()