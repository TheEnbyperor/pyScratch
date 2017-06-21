## PyScratch

Scratch like graphics library in python

Example:
```python
import pyscratch
import time

world = pyscratch.init_world()

cat = pyscratch.get_scratchcat(world)


@pyscratch.on_start(world)
def main():
    cat.rotate(45)
    while True:
        cat.move(10)
        time.sleep(0.2)

world.run()
```