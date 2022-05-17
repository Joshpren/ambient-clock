import threading

from core.ClockController import ClockController
from entities.Hand import Hand
from fsm.StateType import StateType


class Launcher:

    #server = WebServer()
    #server.start_server()
    hour_hand = Hand()
    minute_hand = Hand()
    second_hand = Hand()
    controller = ClockController(120, 0, hour_hand, minute_hand, second_hand)
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
