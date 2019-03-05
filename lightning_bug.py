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
# Use green color value to simulate a Lightning Bug
#

import blinkt
import time
import random

blinkt.set_brightness(0.1)

max_green = [1, 10, 30, 50, 100, 160, 140, 100]           # Set maximum green values for each LED 
green = [0, 0, 0, 0, 0, 0, 0, 0]                          # Set starting values at zero for each LED

def debug_text():                                         # Function to display the raw numbers
    print("LED: {}\tgreen: {}".format(led, green[led]))
    if led == 7:
        print("################")

print("Press Ctrl+C to stop this script...")

try:
    while True:

        ramp = 10                                         # Fade the lights on fast
        while green[5] < max_green[5]:                    # End the loop when the highest value is reached
            for led in range(8):                          # For each of the seven LED's
                green[led] += ramp                        # Increase the LED Green intensity
                if green[led] >= max_green[led]:          # If the Green intensity reaches the max setting...
                    green[led] = max_green[led]           # Stay at that max setting
                blinkt.set_pixel(led, 0, green[led], 0)   # Set the new Green intensity on the LED
                debug_text()                              # Print some debug text to see the numbers
            blinkt.show()                                 # Light up the LED's with the new settings

        ramp = -6                                         # Fade the lights out slower
        while green[5] > 0:                               # End the loop when the lowest value is reached
            for led in range(8):                          # For each of the seven LED's
                green[led] += ramp                        # Decrease the LED Green intensity
                if green[led] <= 0:                       # If the Green intensity reaches zero...
                    green[led] = 0                        # Stay at zero
                blinkt.set_pixel(led, 0, green[led], 0)   # Set the new Green intensity on the LED
                debug_text()                              # Print some debug text to see the numbers
            blinkt.show()                                 # Light up the LED's with the new settings

            if green[led] <= 20:                          # Slow down the last fading lights
                ramp = -2

        pause = random.randint(2, 9)                      # Sleep for a random time before flashing again
        print("Loop Done... sleeping {} seconds".format(pause))
        time.sleep(pause)

except KeyboardInterrupt:
    blinkt.clear()
    blinkt.show()
