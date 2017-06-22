import pygame
import math

GRAD = math.pi / 180


def angle_beetween(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[0]
    rads = math.atan2(-dy, dx)
    rads %= 2 * math.pi
    return math.degrees(rads)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, costumes, world):
        super().__init__()
        if isinstance(costumes, list):
            try:
                image = costumes[0]
                self._costumes = costumes
            except IndexError:
                raise IndexError("Need at least one costume")
        else:
            image = costumes
            self._costumes = [image]
        self._costume = 0
        self._orig_image = world.resources.get_image(image)
        self.image = self._orig_image
        self.rect = self.image.get_rect()
        self.go_to(250, 200)
        self.layer = 0
        self._ddx = 0.0
        self._ddy = 0.0
        self._angle = 0
        self._scale = 1
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
        width, height = self._orig_image.get_size()
        image = pygame.transform.scale(self._orig_image,
                                       (int(width * self._scale),
                                        int(height * self._scale)))
        self.image = pygame.transform.rotate(image, self._angle)
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

    def point_to_mouse(self):
        angle = angle_beetween((self.x_pos, self.y_pos), pygame.mouse.get_pos())
        self.point_in_direction(angle)

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

    def set_scale_to(self, scale):
        self._scale = scale/100

    def change_scale_by(self, scale):
        self._scale += scale/100

    def go_to_top(self):
        self._world.sprites.move_to_front(self)

    def go_to_layer(self, layer):
        self._world.sprites.change_layer(self, layer)

    def next_costume(self):
        self._costume += 1
        if self._costume == len(self._costumes):
            self._costume = 0
        self._update_costume()

    def switch_to_costume(self, costume):
        try:
            self._costume = costume
        except IndexError:
            raise IndexError("Costume not found")
        self._update_costume()

    def _update_costume(self):
        self._orig_image = self._world.resources.get_image(self._costumes[self._costume])

    @property
    def size(self):
        return self._scale

    @property
    def costume(self):
        return self._costume

    #########################
    # Scratch sound section #
    #########################

    def play_sound(self, sound):
        self._world.resources.play_sound(sound)

    def play_sound_until_done(self, sound):
        self._world.resources.play_sound(sound)
        if pygame.mixer.get_busy():
            pass

    def stop_all_sounds(self):
        pygame.mixer.stop()

    def set_volume(self, volume):
        self._world.resources.set_volume(volume/100)

    def change_volume_by(self, volume):
        old_vol = self.volume
        new_vol = old_vol + volume/100
        self._world.resources.set_volume(new_vol)

    @property
    def volume(self):
        return self._world.resources.volume
