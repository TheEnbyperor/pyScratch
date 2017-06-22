import pyscratch
import time

world = pyscratch.init_world()

cat = pyscratch.get_scratchcat(world)


@pyscratch.on_start(world)
def main():
    while True:
        cat.point_to_mouse()
        time.sleep(0.1)

world.run()
