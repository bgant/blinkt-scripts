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
# An attempt to mirror the colors a Cuddlefish uses to mesmorize prey 
#

import blinkt
import time
import random

def led(position, color):
    if color == 'blue':
        blinkt.set_pixel(position, 0, 0, 10)
    elif color == 'white':
        blinkt.set_pixel(position, 0, 10, 10)

color_list = ['blue', 'white'] 

print("Press Ctrl+C to stop this script...")

try:
    while True:
        for color in color_list:
            for x in range(4):
                #print(x, color)
                if x == 0:
                    led(0, color)
                    led(7, color)
                elif x == 1:
                    led(1, color)
                    led(6, color) 
                elif x == 2:
                    led(2, color)
                    led(5, color)
                elif x == 3:
                    led(3, color)
                    led(4, color)
                blinkt.show()
                time.sleep(0.01)

except KeyboardInterrupt:
    blinkt.clear()
    blinkt.show()
