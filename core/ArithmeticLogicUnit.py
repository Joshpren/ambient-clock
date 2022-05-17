from turtle import position


class ArithmeticLogicUnit:

    def __init__(self, number_of_led, position_of_start):
        self.number_of_leds = number_of_led
        self.position_of_start = position


    def switchBy180Degrees(self, index):
        new_index = int(((index + self.number_of_leds / 2) % self.number_of_leds));
        return new_index;

    def getTimeInHours(self, index):
        return int(index / (self.number_of_leds / 60) / 5)

    def getTimeInMinutes(self, index):
        return int(index / (self.number_of_leds / 60))

    def getTimeInSeconds(self, index):
        return int(index / (self.number_of_leds / 60))

    def determine_index_by_hours(self, hours, minutes):
        numberOfLEDsBetweenTwoHours = self.number_of_leds / 12
        ordinalClockRepresentation = hours
        if hours > 12:
            ordinalClockRepresentation -= 12

        delay = int(numberOfLEDsBetweenTwoHours * ( minutes /  60))
        return ordinalClockRepresentation * numberOfLEDsBetweenTwoHours + delay;

    def determine_index_by_minutes(self, minutes, seconds):
        multiplicator = self.number_of_leds / 60
        minutes *= multiplicator
        delay = int(multiplicator * (seconds / 60))

        return minutes + delay

    def determine_index_by_seconds(self, seconds, microseconds):
        multiplicator = self.number_of_leds / 60
        seconds *= multiplicator
        delay = int(microseconds*(10**-6)*2)
        return seconds + delay
