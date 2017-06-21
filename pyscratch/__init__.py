from . import pyScratch
from . import sprite


def init_world():
    return pyScratch.World((500, 400), 60)


def get_scratchcat(world):
    s = sprite.Sprite('scratchcat.png', world)
    world.inject_sprite(s)
    return s


def on_start(world):
    def bind(func):
        world.bind_on_start(func)
        return func
    return bind