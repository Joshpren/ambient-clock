from controller.AbstractController import AbstractController


class TransmissionController(AbstractController):

    def __init__(self, number_of_led):
        self.__time_per_intervall = (60 / number_of_led)*1000

    def seconds_transmission(self, seconds, microseconds, configured_brightness_of_second_hand):
        milliseconds = microseconds*(10**-6)
        seconds_in_Milli = round((seconds + milliseconds) * 1000)
        passed_time_per_intervall = seconds_in_Milli % self.__time_per_intervall

        relative = passed_time_per_intervall / self.__time_per_intervall
        return round(round((1 - relative) * configured_brightness_of_second_hand, 2),1) , round(relative * configured_brightness_of_second_hand, 2)

    def start(self):
        print()

