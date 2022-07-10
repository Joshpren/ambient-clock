from math import ceil
from random import randrange


class Color:

    def __init__(self, red, green, blue):
        self.__red = red
        self.__blue = green
        self.__green = blue
        self.__brightness = 1.0
        self.__white = 0

    @classmethod
    def white(cls, brightness):
        color = cls(255, 255, 255)
        color.brightness = brightness
        return color

    @classmethod
    def random(cls):
        red = randrange(1, 255)
        green = randrange(1, 255)
        blue = randrange(1, 255)
        return cls(red, green, blue)

    @property
    def red(self):
        return int(self.__red * self.__brightness)

    @red.setter
    def red(self, new_red):
        self.__red = new_red

    @property
    def blue(self):
        return int(self.__blue * self.__brightness)

    @blue.setter
    def blue(self, new_blue):
        self.__blue = new_blue

    @property
    def green(self):
        return int(self.__green * self.__brightness)

    @green.setter
    def green(self, new_green):
        self.__green = new_green

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, new_brightness):
        self.__brightness = new_brightness

    @classmethod
    def mix(cls, colors):
        red = 0
        green = 0
        blue = 0
        for color in colors:
            red += color.red
            green += color.green
            blue += color.blue

        red = ceil(red / len(colors))
        green = ceil(green / len(colors))
        blue = ceil(blue / len(colors))
        return Color(red, green, blue)

    @classmethod
    def copy(cls, color, brightness):
        copy_color = Color(color.__red, color.__green, color.__blue)
        copy_color.brightness = brightness
        return copy_color


    def __repr__(self) -> str:
        return "Color(" + str(self.red) + "," + str(self.green) + "," + str(self.blue) + ")"