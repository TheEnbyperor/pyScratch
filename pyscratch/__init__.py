from . import pyScratch
from . import sprite

world = pyScratch.World((500, 400), 60)


def get_scratchcat():
    s = sprite.Sprite('scratchcat.png', world)
    world.inject_sprite(s)
    return s


def get_sprite(img):
    s = sprite.Sprite(img, world)
    world.inject_sprite(s)
    return s


def on_start(func):
    world.bind_on_start(func)
    return func

def run():
    world.run()