import pygame
import threading
from . import resources


class World:
    def __init__(self, size, fps):
        self.resources = resources.Resources()
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("PyScratch")
        self.clock = pygame.time.Clock()
        self.size = size
        self.fps = fps
        self.callbacks = {}
        self.sprites = pygame.sprite.LayeredUpdates()

    def run(self):
        done = False

        for thread in self.callbacks["start"]:
            thread.start()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.sprites.update()

            self.screen.fill((255, 255, 255))

            self.sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)

    def inject_sprite(self, sprite):
        self.sprites.add(sprite)

    def bind_on_start(self, func):
        thread = threading.Thread(target=func, daemon=True)
        cb_list = self.callbacks.get("start", [])
        cb_list.append(thread)
        self.callbacks["start"] = cb_list
