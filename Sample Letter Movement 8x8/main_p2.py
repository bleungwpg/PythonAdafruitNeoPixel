# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
 
import board
import neopixel
 
pixpin = board.D0
numpix = 64
moveLeft = 0

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set brightness to a high value.  1.0 is the maximum value, 0.0 is the lowest
    strip.brightness = 0.1

    for x in range(0, 64):
        strip[x] = (0,0,0)
    strip.write()
    
    # row 1
    strip[0+moveLeft*8] = (255,0,0)
    strip[1+moveLeft*8] = (255,0,0)
    strip[2+moveLeft*8] = (255,0,0)
    strip[3+moveLeft*8] = (255,0,0)
    strip[4+moveLeft*8] = (255,0,0)
    strip[5+moveLeft*8] = (255,0,0)
    strip[6+moveLeft*8] = (255,0,0)
    strip[7+moveLeft*8] = (255,0,0)

    # row 2
    strip[63-0+moveLeft*8] = (255,0,0)
    strip[63-1+moveLeft*8] = (255,0,0)
    strip[63-2+moveLeft*8] = (255,0,0)
    strip[63-3+moveLeft*8] = (255,0,0)
    strip[63-4+moveLeft*8] = (255,0,0)
    strip[63-5+moveLeft*8] = (255,0,0)
    strip[63-6+moveLeft*8] = (255,0,0)
    strip[63-7+moveLeft*8] = (255,0,0)

    # row 3
    strip[8*0+moveLeft*8] = (255,0,0)
    strip[8*1+moveLeft*8] = (255,0,0)
    strip[8*2+moveLeft*8] = (255,0,0)
    strip[8*3+moveLeft*8] = (255,0,0)
    strip[8*4+moveLeft*8] = (255,0,0)
    strip[8*5+moveLeft*8] = (255,0,0)
    strip[8*6+moveLeft*8] = (255,0,0)
    strip[8*7+moveLeft*8] = (255,0,0)

    # row 3
    strip[8*0+7+moveLeft*8] = (255,0,0)
    strip[8*1+7+moveLeft*8] = (255,0,0)
    strip[8*2+7+moveLeft*8] = (255,0,0)
    strip[8*3+7] = (255,0,0)
    strip[8*4+7] = (255,0,0)
    strip[8*5+7] = (255,0,0)
    strip[8*6+7] = (255,0,0)
    strip[8*7+7] = (255,0,0)


    strip.write()
    time.sleep(1)

    moveLeft = moveLeft + 1

    if moveLeft >= 8:
        moveLeft = 0