class ClockPrinter:

    def __init__(self, alu):
        self.__alu = alu


    def printClock(self, hour_diode, minute_diode, second_diode, rainy_minutes):
        stunde = self.__alu.getTimeInHours(hour_diode.index)
        minute = self.__alu.getTimeInMinutes(minute_diode.index)
        sekunde = self.__alu.getTimeInSeconds(second_diode.index)
        print("Wir haben:", stunde, "Uhr", minute, "und", sekunde, "Sekunden.", "Stunden-Index:",
              hour_diode.index, "Stundenzeigerfarbe", hour_diode.color, "Minuten-Index:", minute_diode.index, "Minutenzeigerfarbe", minute_diode.color, "Sekunden-Index:", second_diode.index, "Sekundenzeigerfarbe", second_diode.color, "Regnerische Minuten als Inddex: ", rainy_minutes)