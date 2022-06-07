import datetime
import threading
import time
from abc import ABC
from entities.Diode import Diode
from fsm.State import State
from fsm.StateType import StateType


class WeatherState(State, ABC):
    pass

    def __init__(self, address_led_function, show_diodes_function, switch_to_state_function):
        self.__address_led_function = address_led_function
        self.__show_diodes_function = show_diodes_function
        self.__switch_to_state_function = switch_to_state_function
        self.__weather_data = None
        self.__needs_refresh = True

    def address_leds(self):
        if self.__weather_data == None:
            self.__update_data()
        self.__refresh_if_required()

        for data in self.__weather_data:
            clock = data[0]
            temperature = data[1]
            temperature_index = int(temperature * (self.context.number_of_led/60))
            if(temperature_index >= 0):
                for index in range(temperature_index):
                    self.__address_led_function(Diode(index, self.context.colors_controller.red(100)))
            else:
                for index in range(120, 120 + temperature_index, -1):
                    self.__address_led_function(Diode(index, self.context.colors_controller.blue(100)))
            print(temperature)
            hour_index = self.context.arithmetic_logic_unit.determine_index_by_hours(clock, 0)
            if clock >= 12:
                self.__address_led_function(Diode(hour_index, self.context.colors_controller.blue(100)))
            else:
                self.__address_led_function(Diode(hour_index, self.context.colors_controller.green(100)))
            print(clock)
            self.__show_diodes_function()
            time.sleep(1)
        print(threading.get_native_id())

    def __refresh_if_required(self):
        new_api_call_required = datetime.datetime.now().minute % 3 == 0  # 500 Calls per day therefore ca. 20 calls per hour
        if new_api_call_required:
            if self.__needs_refresh:
                clockThread = threading.Thread(target=self.__load_data, args=())
                clockThread.daemon = True
                clockThread.start()
                clockThread.join()
        else:
            self.__needs_refresh = True

    def __load_data(self):
        print(threading.get_native_id())
        self.context.weather_data_controller.load_weather_data()
        self.__update_data()

    def __update_data(self):
        self.__weather_data = self.context.weather_data_controller.weather_data
        self.__needs_refresh = False

    def react_on_motion(self):
        self.running(False)
        self.__switch_to_state_function(StateType.sundial_state)