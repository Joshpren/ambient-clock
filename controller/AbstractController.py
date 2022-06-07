from abc import ABC, abstractmethod

class AbstractController(ABC):
    pass

    @abstractmethod
    def start(self):
        print()