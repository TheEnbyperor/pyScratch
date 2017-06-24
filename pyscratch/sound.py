import pygame


class Sound:
    def __init__(self, world):
        self._world = world

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

    # TODO: Drum
    # TODO: Note
    # TODO: Instrument
    # TODO: Tempo

    def set_volume(self, volume):
        self._world.resources.set_volume(volume/100)

    def change_volume_by(self, volume):
        old_vol = self.volume
        new_vol = old_vol + volume/100
        self._world.resources.set_volume(new_vol)

    @property
    def volume(self):
        return self._world.resources.volume
