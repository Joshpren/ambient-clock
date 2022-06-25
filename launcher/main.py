import threading

from controller.WeatherDataController import WeatherDataController
from controller.ClockController import ClockController
from controller.ColorsController import ColorController
from entities.Color import Color
from fsm.StateType import StateType


class Launcher:

    color_controller = ColorController.init()
    weather_data_controller = WeatherDataController.init()
    controller = ClockController.init(int(input("Wie viele LEDs werden verwendet")), 0, color_controller, weather_data_controller)
    clockThread = threading.Thread(target=controller.start, args=())
    clockThread.daemon = True
    clockThread.start()

    try:
        while True:
            userInput = input()
            if userInput == "q":
                running = False
                print("Exit")
            elif userInput == "1":
                controller.react_on_motion()
            elif userInput == "e":
                color_controller.hour_hand_color = Color.random()
            elif userInput == "a":
                controller.switch_to_state(StateType.ambient_state)
            elif userInput == "w":
                controller.switch_to_state(StateType.weather_state)
            elif userInput == "o":
                controller.switch_to_state(StateType.ordinal_state)
            print(threading.get_native_id())
    except KeyboardInterrupt:
        pass



    SystemExit
