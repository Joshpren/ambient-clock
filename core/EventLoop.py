from threading import Thread, Event


class EventLoop:

    def __init__(self, runnable):
        self.__runnable = runnable
        self.__event = None
        self.__running_thread = None


    def run(self):
        event = Event()
        self.__event = event
        self.__running_thread = Thread(target=self.__run_runnable, args=())
        self.__running_thread.start()

    def __run_runnable(self):
        while not self.__event.is_set():
            self.__runnable()


    def stop(self, clear_function):
        self.__event.set()
        self.__running_thread.join()
        if clear_function:
            clear_function()
