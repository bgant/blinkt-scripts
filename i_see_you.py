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
# You can see the individual red, green, blue LED dots in each RGB LED
#

import blinkt

try:
    while True:
        blinkt.set_all(1, 1, 1)
        blinkt.show()

except KeyboardInterrupt:
    pass

