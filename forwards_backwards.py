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
# Showing how to use variables and if statements 
#

import time
import blinkt

x = 0  # Initial starting number

while True:
    if x == 0:
        direction = 1 

    if x == 7:
        direction = -1

    print("x is", x)

    blinkt.clear()
    blinkt.set_pixel(x, 0, 0, 10)
    blinkt.show() 

    x += direction

    time.sleep(0.4)

