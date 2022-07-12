import random
import time
from abc import ABC
from entities.Color import Color
from entities.Diode import Diode
from fsm.StateType import StateType
from fsm.State import State

class AmbientState(State, ABC):
    pass

    def __init__(self, switch_to_state_function):
        self.__switch_to_state_function = switch_to_state_function


    def run(self):
        self.address_leds()

    def address_leds(self):
        self.color_wipe()

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.sundial_state)

    def color_wipe(self):
        color = self.service.colors_controller.random()
        for index in range(self.service.led_count):
            self.service.led_event_handler.address_diode(Diode(index, color))
            self.service.led_event_handler.show()
            time.sleep(0.2)

    #def rainbow(self):
        #for j in range(256):
            #for index in range(self.service.led_count):
                #self.service.led_event_handler.address_diode(Diode(index, Color(wheel((index + j) & 255))
            #self.service.led_event_handler.show()
            #time.sleep(20 / 1000.0)

    def aurora(self):
        #init nightsky
        aurora_color_palette = (Color(3, 130, 152), Color(1, 82, 104), Color(4, 226, 183), Color(14, 243, 197), Color(181,61,255), Color(141,0,196))
        night_sky_color = (Color(0,7,74), Color(2, 83, 133), Color(23, 35, 71))
        for index in range(self.service.led_count):
            self.service.led_event_handler.address_diode(Diode(index, night_sky_color))

    def build_aurora(self):
        random.randint(6,)

    class Aurora:

        def __init__(self):
            self.__start = random.randint(self.service.led_count)
            self.__end = (self.__start + self.service.led_count) % self.service.led_count