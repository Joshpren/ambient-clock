class Diode:

    def __init__(self, index):
        self.__index = index
        self.__brightness = 100
        self.__red = 255
        self.__blue = 255
        self.__green = 255
        self.__white = None

    @property
    def index(self):
        return self.__index

    @property
    def brightness(self):
        return self.__brightness

    @property
    def red(self):
        return self.__red

    @property
    def blue(self):
        return self.__blue

    @property
    def green(self):
        return self.__green

    @property
    def white(self):
        return self.__white
