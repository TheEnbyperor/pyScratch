import pygame
import os


class Resources:
    def __init__(self):
        self._image_library = {}
        self._sound_library = {}

    def get_image(self, path):
        image = self._image_library.get(path)
        if image is None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            self._image_library[path] = image
        return image

    def play_sound(self, path):
        sound = self._sound_library.get(path)
        if sound == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            sound = pygame.mixer.Sound(canonicalized_path)
            self._sound_library[path] = sound
        sound.play()
