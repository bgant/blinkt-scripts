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
# Using random module to set LED's to a random color value
#

import blinkt 
import random
import time

while True:
    for pixel in range(8):
        r = random.randint(0, 80)
        g = random.randint(0, 80)
        b = random.randint(0, 80)
        print(pixel, r, g, b)
        blinkt.set_pixel(pixel, r, g, b)
        blinkt.show()
        time.sleep(0.5)
