import pygame
import math

GRAD = math.pi / 180


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, world):
        super().__init__()

        self._orig_image = world.resources.get_image(image)
        self.image = self._orig_image
        self.rect = self.image.get_rect()
        self.go_to(250, 200)
        self._ddx = 0.0
        self._ddy = 0.0
        self._angle = 0
        self._world = world
        self._hidden = False

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > self._world.size[0]:
            self.rect.x = self._world.size[0]
        if self.rect.y > self._world.size[1]:
            self.rect.y = self._world.size[1]
        self.image = pygame.transform.rotate(self._orig_image, self._angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self):
        if not self._hidden:
            self._world.blit(self.image, self.rect)

    ########################
    # Scratch move section #
    ########################

    def move(self, steps):
        self._ddx = +math.cos(self._angle * GRAD)
        self._ddy = -math.sin(self._angle * GRAD)
        self.rect.x += self._ddx * steps
        self.rect.y += self._ddy * steps

    def turn(self, degrees):
        self._angle += degrees

    def point_in_direction(self, degrees):
        self._angle = degrees

    def go_to(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def go_to_mouse(self):
        x, y = pygame.mouse.get_pos()
        self.go_to(x, y)

    def set_x(self, x):
        self.rect.x = x - (self.image.get_width() / 2)

    def change_x_by(self, x):
        self.rect.x += x

    def set_y(self, y):
        self.rect.y = y - (self.image.get_height() / 2)

    def change_y_by(self, y):
        self.rect.y += y

    def angle_beetween(self, a, b):
        math.atan2(a[1], a[0])
        math.atan2(b[1], b[0])

    @property
    def x_pos(self):
        return self.rect.x

    @property
    def y_pos(self):
        return self.rect.y

    @property
    def direction(self):
        return self._angle

    #########################
    # Scratch looks section #
    #########################

    def show(self):
        self._hidden = False

    def hide(self):
        self._hidden = True
