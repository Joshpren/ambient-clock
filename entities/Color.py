from random import randrange


class Color:

    def __init__(self, red, green, blue):
        self.__red = red
        self.__blue = green
        self.__green = blue
        self.__white = 0

    @classmethod
    def white(cls, brightness):
        if(brightness < 0 or brightness > 255):
            return cls(0, 0, 0)
        return cls(brightness, brightness, brightness)

    @classmethod
    def random(cls):
        red = randrange(1, 255)
        green = randrange(1, 255)
        blue = randrange(1, 255)
        return cls(red, green, blue)

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

    def __repr__(self) -> str:
        return "Color(" + str(self.__red) + "," + str(self.__green) + "," + str(self.__blue) + ")"

