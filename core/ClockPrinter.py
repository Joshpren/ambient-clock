class ClockPrinter:

    def __init__(self, alu):
        self.__alu = alu


    def printClock(self, hour_hand_index, minute_hand_index, second_hand_index):
        stunde = self.__alu.getTimeInHours(hour_hand_index)
        minute = self.__alu.getTimeInMinutes(minute_hand_index)
        sekunde = self.__alu.getTimeInSeconds(second_hand_index)
        print("Wir haben:", stunde, "Uhr", minute, "und", sekunde, "Sekunden.", "Stunden-Index:",
              hour_hand_index, "Minuten-Index:", minute_hand_index, "Sekunden-Index:", second_hand_index)