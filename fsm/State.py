from abc import ABC, abstractmethod


class State(ABC):
    pass

    def __init__(self, runnable):
        self.runnable = runnable
        self.__running = False

    def start(self):
        self.running(True)
        self.address_leds()

    @abstractmethod
    def address_leds(self):
        print()

    @abstractmethod
    def react_on_motion(self):
        print()


    def running(self, running):
        self.__running = running

    @property
    def get_running(self):
        return self.__running