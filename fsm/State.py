from abc import ABC, abstractmethod


class State(ABC):
    pass

    def __init__(self):
        self.__running = False
        self.__context = None

    def start(self, context):
        self.__context = context
        self.running(True)
        self.address_leds()

    @property
    def context(self):
       return self.__context

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