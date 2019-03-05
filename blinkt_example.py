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
# Program to teach how while and for loops work
#

import time					# load   time module commands
import blinkt					# load blinkt module commands

blinkt.set_clear_on_exit()			# turn off all LED's when program ends
blinkt.set_brightness(0.1)			# set brightness on all LED's to lowest setting
print('Type Ctrl+C to end this program...')	# remind user how to stop this program

blinkt.set_all(200, 100, 0)			# set all LED's to Yellow light
blinkt.show()					# show LED settings
time.sleep(2)					# wait 2 seconds

while True:					# Run continuously in a loop
    blinkt.set_all(255, 40, 0)			# set all LED's to Orange light
    blinkt.show()				# show LED settings
    time.sleep(1)				# wait 1 second
    for x in range(8):				# for each LED (x) in numbers 0 to 7
        #blinkt.clear()				# turn off all LED's
        blinkt.set_pixel(x, 80, 0, 80)		# set LED (x) to Purple light
        blinkt.show()				# show LED settings
        time.sleep(0.1)				# wait 0.1 seconds

