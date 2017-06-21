import pygame
import math

GRAD = math.pi / 180


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, world):
        super().__init__()

        self.orig_image = world.resources.get_image(image)
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 200
        self.ddx = 0.0
        self.ddy = 0.0
        self.angle = 0
        self.world = world

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > self.world.size[0]:
            self.rect.x = self.world.size[0]
        if self.rect.y > self.world.size[1]:
            self.rect.y = self.world.size[1]
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, steps):
        self.ddx = +math.cos(self.angle * GRAD)
        self.ddy = -math.sin(self.angle * GRAD)
        self.rect.x += self.ddx * steps
        self.rect.y += self.ddy * steps

    def rotate(self, degres):
        self.angle += degres

