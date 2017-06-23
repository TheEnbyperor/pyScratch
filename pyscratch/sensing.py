import pygame
import time


class Sensing:
    def __init__(self, world):
        self._world = world
        self._time = time.time()

    ###########################
    # Scratch sensing section #
    ###########################

    # TODO: Ask question

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

    @property
    def timer(self):
        return time.time() - self._time
