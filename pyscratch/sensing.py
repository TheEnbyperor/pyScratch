import pygame
import time
import threading


class Sensing:
    def __init__(self, world):
        self._world = world
        self._time = time.time()
        self._timer_event = []
        self._timer_thread = threading.Thread(target=self._timer_thread_func, daemon=True)
        self._timer_thread.start()

    def _timer_thread_func(self):
        while True:
            for func in self._timer_event:
                if func["timer"] > self.timer and func["called"] is False:
                    func()
                    func["called"] = True
            time.sleep(0.05)

    def add_timer_event(self, event):
        self._timer_event.append(event)

    ###########################
    # Scratch sensing section #
    ###########################

    # TODO: Ask question
    # TODO: Key pressed
    # TODO: Time
    # TODO: Days since 2000

    @property
    def mouse_x(self):
        x, _ = pygame.mouse.get_pos()
        return x

    @property
    def mouse_y(self):
        _, y = pygame.mouse.get_pos()
        return y

    @property
    def mouse_down(self):
        return pygame.mouse.get_pressed()

    def reset_timer(self):
        self._time = time.time()
        for func in self._timer_event:
            func["called"] = False


    @property
    def timer(self):
        return time.time() - self._time
