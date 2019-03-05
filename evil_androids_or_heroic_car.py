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
# This is a convoluted attempt at a "Larson Scanner":
#   https://wiki.evilmadscientist.com/Larson_Scanner
#
# The brightness setting is hard to adjust. A better solution would
# be to use the red color setting to adjust the brightness
#

import blinkt
import time 

blinkt.clear()  # Clear LED's

# The idea is that the leading LED is at 100%, the next at 75%, 50%, etc. 
# They then follow each other across the LED bar
i = {0:0, 25:1, 50:2, 75:3, 100:4}          # Initialize Starting Brightness
direction = {0:1, 25:1, 50:1, 75:1, 100:1}  # Initialize Starting Direction

print("Press Ctrl+C to stop this script...")

try:
    while True:
        for n in (0,25,50,75,100): # For each brightness level
            if i[n] == 7:  # Upper Bound LED
                direction[n] = -1  # Reverse direction
            if i[n] == 0:  # Lower Bound LED
                direction[n] =  1  # Forward direction
            i[n] = i[n] + direction[n]
    
        #print(i[0], i[25], i[50], i[75], i[100])
        blinkt.set_pixel(i[0],   100, 0, 0, 0.00) # Trailing LED's will stay at low Brightness
        blinkt.set_pixel(i[25],  100, 0, 0, 0.05) # Adjust brightness of each pixel to get a clean look
        blinkt.set_pixel(i[50],  100, 0, 0, 0.10)
        blinkt.set_pixel(i[75],  100, 0, 0, 0.20)
        blinkt.set_pixel(i[100], 100, 0, 0, 0.30)
        blinkt.show()
        time.sleep(0.1)

except KeyboardInterrupt:
    blinkt.clear()
    blinkt.show()
