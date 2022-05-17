class Hand:

    def __init__(self):
        self.__index = 0
        self.__brightness = 100
        self.__red = 255
        self.__blue = 255
        self.__green = 255
        self.__white = 0

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, new_index):
        self.__index = new_index

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, new_brightness):
        self.__brightness = new_brightness

    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, new_red):
        self.__red = new_red

    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, new_blue):
        self.__blue = new_blue

    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, new_green):
        self.__green = new_green

    @property
    def white(self):
        return self.__white

    @white.setter
    def white(self, new_white):
        self.__white = new_white

