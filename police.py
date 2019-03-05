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
# Homework assignment:
#   Flash First  Half of LED's Red  three times
#   Flash Second Half of LED's Blue three times
#   Repeat
#

import blinkt
import time

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

print("Press Ctrl+C to stop script...")

try:
    while True:
        # Blink Red Three Times
        for x in range(3):
            # Turn lights on
            blinkt.set_pixel(0,255,0,0)
            blinkt.set_pixel(1,255,0,0)
            blinkt.set_pixel(2,255,0,0)
            blinkt.set_pixel(3,255,0,0)
            blinkt.show()
            time.sleep(0.02)
        
            # Turn lights off
            blinkt.clear()
            blinkt.show()
            time.sleep(0.02)

        # Blink Blue Three Times
        for x in range(3):
            # Turn lights on
            blinkt.set_pixel(4,0,0,255)
            blinkt.set_pixel(5,0,0,255)
            blinkt.set_pixel(6,0,0,255)
            blinkt.set_pixel(7,0,0,255)
            blinkt.show()
            time.sleep(0.02)

            # Turn lights off
            blinkt.clear()
            blinkt.show()
            time.sleep(0.02)

except KeyboardInterrupt:
    blinkt.clear()
    blinkt.show()

