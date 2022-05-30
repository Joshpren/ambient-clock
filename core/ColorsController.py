from entities.Color import Color


class ColorController:

    def __init__(self):
        self.__colors_to_use = []
        self.__hour_hand_color = Color.white(150)
        self.__minute_hand_color = Color.white(200)
        self.__second_hand_color = Color.white(255)

    @property
    def colors_to_use(self):
        if len(self.__colors_to_use) == 0:
            return [Color.random() * 4]
        else:
            return self.__colors_to_use

    def red(self, brightness):
        return Color(brightness, 0, 0)

    def green(self, brightness):
        return Color(0, brightness, 0)

    def blue(self, brightness):
        return Color(0, 0, brightness)

    def random(self):
        return Color.random()

    @colors_to_use.setter
    def colors_to_use(self, new_colors_to_use):
        self.__colors_to_use = new_colors_to_use

    @property
    def hour_hand_color(self):
        return self.__hour_hand_color

    @hour_hand_color.setter
    def hour_hand_color(self, new_color):
        self.__hour_hand_color = new_color

    @property
    def minute_hand_color(self):
        return self.__minute_hand_color

    @minute_hand_color.setter
    def minute_hand_color(self, new_color):
         self.__minute_hand_color = new_color

    @property
    def second_hand_color(self):
        return self.__second_hand_color

    @second_hand_color.setter
    def second_hand_color(self, new_color):
        self.__second_hand_color = new_color