class Context:

    def __init__(self, alu, colors_controller, number_of_led):
        self.__arithmetic_logic_unit = alu
        self.__colors_controller = colors_controller
        self.__number_of_led = number_of_led

    @property
    def number_of_led(self):
        return self.__number_of_led

    @property
    def arithmetic_logic_unit(self):
        return self.__arithmetic_logic_unit

    @property
    def colors_controller(self):
        return self.__colors_controller