import pyscratch
import time

world = pyscratch.init_world()

cat = pyscratch.get_scratchcat(world)


@pyscratch.on_start(world)
def main():
    while True:
        cat.go_to_mouse()
        time.sleep(0.1)

world.run()
