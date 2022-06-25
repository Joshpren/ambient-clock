from controller.AbstractController import AbstractController


class TransmissionController(AbstractController):

    def transmission(self, microseconds):
      milliseconds = microseconds*(10**-6)
      return (1 - milliseconds), milliseconds

    def start(self):
        print()