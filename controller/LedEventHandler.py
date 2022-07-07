from core.ClockPrinter import ClockPrinter


class LedEventHandler:

    def __init__(self, led_strip):
        self.__led_strip = led_strip

    @property
    def led_count(self) -> int:
        return self.__led_strip.led_count

    def address_diode(self, diode):
        self.__led_strip.address_diode(diode)

    def turn_off_diode(self, index):
        self.__led_strip.turn_off_diode(index)

    def show(self):
        self.__led_strip.show()

    def show_hands(self):
        self.__led_strip.show_hands()
