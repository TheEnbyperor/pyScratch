## PyScratch

Scratch like graphics library in python

Example:
```python
import pyscratch
import time

cat = pyscratch.get_scratchcat()


@pyscratch.on_start
def main():
    cat.set_scale_to(125)
    while True:
        cat.point_to_mouse()
        time.sleep(0.1)

pyscratch.run()

```
![Example running](https://raw.githubusercontent.com/benjaminmisell/pyScratch/master/scratchcat.svg)
