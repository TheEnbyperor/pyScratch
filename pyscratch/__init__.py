import pyscratch.pyScratch
import pyscratch.sprite
import pyscratch.sound
import pyscratch.sensing
import pyscratch.events

world = pyscratch.pyScratch.World((500, 400), 60)
sound = pyscratch.sound.Sound(world)
sensing = pyscratch.sensing.Sensing(world)
events = pyscratch.events.Events(world)


def get_scratchcat():
    s = pyscratch.sprite.Sprite('scratchcat.png', world)
    world.inject_sprite(s)
    return s


def get_sprite(img):
    s = pyscratch.sprite.Sprite(img, world)
    world.inject_sprite(s)
    return s


def run():
    world.run()
