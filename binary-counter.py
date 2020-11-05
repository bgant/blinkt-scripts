# Source Idea: LXF251 Page 56

import blinkt
from time import sleep

count=0
blinkt.clear()
blinkt.set_brightness(0.1)

def toggle(LED,STATE):
    if STATE is 1:
        blinkt.set_pixel(LED,0,0,255)
    else:
        blinkt.set_pixel(LED,0,0,0)

while True:
    count=(count + 1) % 256  # Modulo counter returns to zero at 256
    BINARY_COUNT='{:08b}'.format(count)
    print(BINARY_COUNT)
    for LED in range(8):
        toggle(LED,BINARY_COUNT[LED])
    blinkt.show()
    sleep(0.2)

