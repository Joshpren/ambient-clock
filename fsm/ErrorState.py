import logging
import time
from abc import ABC
from entities.Diode import Diode
from fsm.State import State


class ErrorState(State, ABC):
    pass

    def __init__(self, switch_to_state_function):
        self.__switch_to_state_function = switch_to_state_function

    def start(self):
        logging.info("Error-State has been started!")
        print("Error-State has been started!")

    def run(self, event):
        while not event.is_set():
            self.address_leds()

    def address_leds(self):
        for brightness in range(1,100):
            for index in range(self.service.led_count):
                red_by_brightness = self.service.colors_controller.red(brightness/100)
                self.service.led_event_handler.address_diode(Diode(index, red_by_brightness))
            self.service.led_event_handler.show()
            time.sleep(0.02)
        for brightness in range(100, 0, -1):
            for index in range(self.service.led_count):
                red_by_brightness = self.service.colors_controller.red(brightness/100)
                self.service.led_event_handler.address_diode(Diode(index, red_by_brightness))
            self.service.led_event_handler.show()
        time.sleep(0.02)

    def react_on_motion(self):
        pass

    def clear(self):
        logging.info("Error-State has been cleared")