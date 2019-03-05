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
# Playing with how to set r,g,b, values using color names
#

import blinkt
import time
import random

def led(position, color):
    if color == 'red':
        blinkt.set_pixel(position, 30, 0, 0)
    elif color == 'green':
        blinkt.set_pixel(position, 0, 30, 0)
    elif color == 'blue':
        blinkt.set_pixel(position, 0, 0 , 30)
    elif color == 'purple':
        blinkt.set_pixel(position, 30, 0, 30)
    elif color == 'yellow':
        blinkt.set_pixel(position, 30, 15, 0)
    elif color == 'orange':
        blinkt.set_pixel(position, 30, 5, 0)
    else:
        blinkt.set_pixel(position, 20, 20, 20)

color_list = ['red', 'green', 'blue', 'purple', 'yellow', 'orange'] 

print("Press Ctrl+C to stop this script...")

try:
    while True:
        random.shuffle(color_list)
        for color in color_list:
            for x in range(4):
                #print(x, color)
                if x == 3:
                    led(0, color)
                    led(7, color)
                elif x == 2:
                    led(1, color)
                    led(6, color) 
                elif x == 1:
                    led(2, color)
                    led(5, color)
                elif x == 0:
                    led(3, color)
                    led(4, color)
                blinkt.show()
                time.sleep(0.02)

except KeyboardInterrupt:
    blinkt.clear()
    blinkt.show()
