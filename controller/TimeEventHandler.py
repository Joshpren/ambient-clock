import datetime


class TimeEventController:

    def __init__(self):
        self.__last_hour = datetime.datetime.now().hour
        self.__last_day = datetime.datetime.now().day
        self.__last_year = datetime.datetime.now().year
        self.__event_listeners = []


    def scan_time(self):
        current_time = datetime.datetime.now()
        self.__new_hour(current_time)
        self.__new_day(current_time)
        self.__new_year(current_time)

    def __new_hour(self, current_time):
        is_new_hour = current_time.minute % 60 == 0 and current_time.hour != self.__last_hour
        if(is_new_hour):
            self.__last_hour = current_time.hour
            self.__inform_listener()

    def __new_day(self, current_time):
        is_new_day = current_time.day != self.__last_day
        if (is_new_day):
            self.__last_day = current_time.day
            self.__inform_listener()

    def __new_year(self, current_time):
        is_new_year = current_time.year != self.__last_year
        if (is_new_year):
            self.__last_day = current_time.day
            self.__inform_listener()

    def __inform_listener(self, effect):
        for event_listener in self.__event_listeners:
            event_listener(effect)

    def add_event_listener(self, event_listener):
        self.__event_listeners.append(event_listener)

    def remove_event_listener(self, event_listener):
        self.__event_listeners.remove(event_listener)
