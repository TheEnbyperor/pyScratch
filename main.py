import pyscratch
import time

cat = pyscratch.get_scratchcat()


@pyscratch.events.on_start
def main():
    cat.set_scale_to(125)
    # pyscratch.sound.play_sound("meow.wav")
    while True:
        cat.point_to_mouse()
        time.sleep(0.1)


pyscratch.run()
