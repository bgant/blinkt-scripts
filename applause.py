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
# Tutorial:
#   https://www.pygame.org/docs/ref/mixer.html
#
# Play .wav file with Python
#

from pygame import mixer

mixer.init()
#mixer.fadeout(1000)
sound = mixer.Sound('applause-1.wav')
sound.play()
