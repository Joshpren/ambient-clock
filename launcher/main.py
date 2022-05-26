import threading

from core.ClockController import ClockController
from core.ColorsController import ColorController
from entities.Hand import Hand
from fsm.StateType import StateType


class Launcher:

    color_controller = ColorController()
    controller = ClockController(12, 0, color_controller)
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
        elif userInput == "s":
            controller.switch_to_state(StateType.ambient_state)



    SystemExit
