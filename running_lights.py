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
# Simple script to teach while and for loops
#

import blinkt
import time

while True:
    for led in range(8):
        blinkt.clear()
        blinkt.set_pixel(led, 0, 0, 255)
        blinkt.show()
        time.sleep(0.05)

