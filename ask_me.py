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
# Demonstrate asking for input to light up LED
#

import time
import blinkt

# Clear the Linux Terminal screen
import os
os.system('clear')

count = 1  # Initial starting count

while count <= 3:

    led = input("Which LED should I light up? ")
    led = int(led)  # Convert String (text) to Integer (number)

    if ( led >= 0 ) and ( led <= 7 ):
        print("I will light up LED number", led)
        print("")
        blinkt.clear()
        blinkt.set_pixel(led, 0, 0, 10)
        blinkt.show()
    else:
        print("You need to pick a number from 0 to 7")
        print("")

    time.sleep(3)

    # Turn off all LED's
    blinkt.clear()
    blinkt.show()

    count += 1

