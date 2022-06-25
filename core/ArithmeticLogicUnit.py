class ArithmeticLogicUnit:

    def __init__(self, number_of_led, position_of_start):
        self.number_of_leds = number_of_led
        self.position_of_start = position_of_start


    def __switchBy180Degrees(self, index):
        new_index = int(((index + self.number_of_leds / 2) % self.number_of_leds))
        return new_index

    def relative_position_of_start(self, real_index) -> int:
        relative_index = int(((real_index + self.position_of_start) % self.number_of_leds))
        return relative_index

    def __revert_relative_index(self, relativ_index) -> int:
        absolute_index = ((relativ_index - self.position_of_start) + self.number_of_leds) % self.number_of_leds
        return absolute_index

    def getTimeInHours(self, index):
        return int(self.__revert_relative_index(index)  / (self.number_of_leds / 60) / 5)

    def getTimeInMinutes(self, index):
        return int(self.__revert_relative_index(index) / (self.number_of_leds / 60))

    def getTimeInSeconds(self, index):
        return int(self.__revert_relative_index(index) / (self.number_of_leds / 60))

    def determine_index_by_hours(self, hours, minutes):
        numberOfLEDsBetweenTwoHours = self.number_of_leds / 12
        ordinalClockRepresentation = hours
        if hours > 12:
            ordinalClockRepresentation -= 12
        delay = int(numberOfLEDsBetweenTwoHours * (minutes /  60))
        absolut_hour_index = int(ordinalClockRepresentation * numberOfLEDsBetweenTwoHours + delay)
        return self.relative_position_of_start(absolut_hour_index)

    def determine_index_by_minutes(self, minutes, seconds):
        multiplicator = self.number_of_leds / 60
        minutes *= multiplicator
        delay = int(multiplicator * (seconds / 60))
        absolut_minute_index = int(minutes + delay)
        return self.relative_position_of_start(absolut_minute_index)

    def determine_index_by_seconds(self, seconds, microseconds):
        multiplicator = self.number_of_leds / 60
        seconds *= multiplicator
        delay = int(microseconds*(10**-6)*int(multiplicator))
        absolut_second_index = int(seconds + delay)
        return self.relative_position_of_start(absolut_second_index)

    def determine_sundial_index_by_hours(self, hours, minutes):
        return self.__switchBy180Degrees(self.determine_index_by_hours(hours, minutes))

    def determine_sundial_index_by_minutes(self, minutes, seconds):
        return self.__switchBy180Degrees(self.determine_index_by_minutes(minutes, seconds))

    def determine_sundial_index_by_seconds(self, seconds, microseconds):
        return self.__switchBy180Degrees(self.determine_index_by_seconds(seconds, microseconds))