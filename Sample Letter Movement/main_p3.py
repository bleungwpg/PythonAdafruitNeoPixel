# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
 
import board
import neopixel
 
pixpin = board.D0
numpix = 64
moveLeft = -8

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set brightness to a high value.  1.0 is the maximum value, 0.0 is the lowest
    strip.brightness = 0.1

    for x in range(0, 64):
        strip[x] = (0,0,0)
    strip.write()
    
    # row 1
    for x in range(0, 8):
        temp = x+moveLeft*8
        if temp >= 0 and temp < 64:
            strip[temp] = (255,0,0)

    # row 2
    for x in range(0, 8):
        temp = 63-x+moveLeft*8
        if temp >= 0 and temp < 64:
            strip[temp] = (255,0,0)


    # row 3
    for x in range(0, 8):
        temp = 8*x+moveLeft*8
        if temp >= 0 and temp < 64:
            strip[temp] = (255,0,0)

    # row 4
    for x in range(0, 8):
        temp = 8*x+7+moveLeft*8
        if temp >= 0 and temp < 64:
            strip[temp] = (255,0,0)


    strip.write()
    time.sleep(0.2)

    moveLeft = moveLeft + 1

    if moveLeft >= 8:
        moveLeft = -8