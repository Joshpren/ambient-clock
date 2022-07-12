from entities.Color import Color

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

    def address_diode(self, index, red, green, blue):
        self.__active_diodes.append(index)
        self.__strip[index] = Color(red, green, blue)

    def turn_off_diode(self, index):
        self.__strip[index] = Color(0, 0, 0)

    def clear_strip(self):
        for index in self.__active_diodes:
            self.turn_off_diode(index)
        self.__active_diodes.clear()

    def show(self):
        print(self.__strip)