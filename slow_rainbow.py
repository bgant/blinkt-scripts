# Pimoroni Blinkt!:
#   https://shop.pimoroni.com/products/blinkt
#   https://www.sparkfun.com/products/14038
#
# Raspberry Pi:
#   https://www.raspberrypi.org/
#   https://www.sparkfun.com/products/14643
#
# Source: 
#   https://github.com/bgant/blinkt
#
# Modified from Pimoroni Blinkt github example script rainbow.py:
#   https://github.com/pimoroni/blinkt/blob/master/examples/rainbow.py
#

import colorsys
import time
import blinkt

intensity = 50  # Between 20 and 255 

spacing = 360.0 / 16.0
hue = 0

blinkt.set_brightness(0.1)

try:
    while True:
        hue = int(time.time() * 5) % 360
        h = ((hue) % 360) / 360.0
        r, g, b = [int(c * intensity) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        blinkt.set_all(r, g, b)
        blinkt.show()
        time.sleep(0.001)

except KeyboardInterrupt:
    time.sleep(0.2)
    blinkt.clear()
    blinkt.show()

