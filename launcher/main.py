import threading

from core.ClockController import ClockController
from core.ColorsController import ColorController
from entities.Color import Color
from fsm.StateType import StateType


class Launcher:

    color_controller = ColorController()
    controller = ClockController(int(input()), 0, color_controller)
    clockThread = threading.Thread(target=controller.start, args=())
    clockThread.daemon = True
    clockThread.start()
    running = True
    while running:
        userInput = input()
        if userInput == "q":
            running = False
            print("Exit")
        elif userInput == "1":
            controller.react_on_motion()
        elif userInput == "e":
            color_controller.hour_hand_color = Color.random()
        elif userInput == "s":
            controller.switch_to_state(StateType.ambient_state)



    SystemExit
