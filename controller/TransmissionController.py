from controller.AbstractController import AbstractController


class TransmissionController(AbstractController):

    def __init__(self, number_of_led):
        self.__time_per_intervall = (60 / number_of_led)*1000
        self.__millisecond_steps_per_minute_intervall = ((60 / number_of_led) * 60) * 1000
        self.__second_steps_per_hour_intervall = (60 / (number_of_led/12))*60

    def transmission(self, hand, time):
        darkening, brightnening = 1, 1
        if "hour" == hand:
            darkening, brightnening = self.hour_transmission(time.minute, time.second)
        elif "minute" == hand:
            darkening, brightnening = self.minute_transmission(time.second, time.microsecond)
        elif "second" == hand:
            darkening, brightnening = self.second_transmission(time.second, time.microsecond)

        return round(darkening, 2), round(brightnening, 2)

    def hour_transmission(self, minutes, seconds):
        passed_time_in_seconds = minutes * 60 + seconds
        passed_time_per_intervall = passed_time_in_seconds % self.__second_steps_per_hour_intervall
        relative = passed_time_per_intervall / self.__second_steps_per_hour_intervall
        return (1 - relative), relative

    def minute_transmission(self, seconds, microseconds):
        milliseconds = microseconds * (10 ** -6)
        passed_time_in_milliseconds = seconds * 1000 + milliseconds
        passed_time_per_intervall = passed_time_in_milliseconds % self.__millisecond_steps_per_minute_intervall
        relative = passed_time_per_intervall / self.__millisecond_steps_per_minute_intervall
        return (1 - relative), relative

    def second_transmission(self, seconds, microseconds):
        milliseconds = microseconds*(10**-6)
        seconds_in_Milli = round((seconds + milliseconds) * 1000)
        passed_time_per_intervall = seconds_in_Milli % self.__time_per_intervall

        relative = passed_time_per_intervall / self.__time_per_intervall
        return (1 - relative), relative


    def start(self):
        print()

