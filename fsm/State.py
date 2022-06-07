from abc import ABC, abstractmethod


class State(ABC):
    pass

    def __init__(self):
        self.__service_provider = None

    def init(self, service):
        self.__service_provider = service
        self.start()

    @property
    def service(self):
       return self.__service_provider

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

    @abstractmethod
    def clear(self):
        print()