class Diode:

    def __init__(self, index, color):
        self.__index = index
        self.__color = color


    @property
    def index(self):
        return self.__index

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    def __repr__(self) -> str:
        return "Diode: " + str(self.index) + ", " + str(self.__color)
