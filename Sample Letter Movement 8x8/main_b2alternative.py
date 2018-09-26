# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
 
import board
import neopixel
 
pixpin = board.D0
numpix = 64

move = 8

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set brightness to a high value.  1.0 is the maximum value, 0.0 is the lowest
    strip.brightness = 0.1
    
    for x in range(0, 64):
        strip[x] = (0,0,0)
    strip.write()

    # All the horizontal lines
    temp = 2 + move
    if temp >= 0 and temp < 8:
        strip[temp] = (255,0,0)
    temp = 3 + move
    if temp >= 0 and temp < 8:
        strip[temp] = (255,0,0)
    temp = 4 + move
    if temp >= 0 and temp < 8:
        strip[temp] = (255,0,0)


    temp = 8*3+3 + move
    if temp >= 8*3 and temp < 8*4:
        strip[temp] = (255,0,0)
    temp = 8*3+4 + move
    if temp >= 8*3 and temp < 8*4:
        strip[temp] = (255,0,0)


    temp = 8*7+3 + move
    if temp >= 8*7 and temp < 8*8:
        strip[temp] = (255,0,0)
    temp = 8*7+4 + move
    if temp >= 8*7 and temp < 8*8:
        strip[temp] = (255,0,0)



    # All the vertical lines
    temp = 8*1+2 + move
    if temp >= 8*1 and temp < 8*2:
        strip[temp] = (255,0,0)
    temp = 8*2+2 + move
    if temp >= 8*2 and temp < 8*3:
        strip[temp] = (255,0,0)
    temp = 8*3+2 + move
    if temp >= 8*3 and temp < 8*4:
        strip[temp] = (255,0,0)
    temp = 8*4+2 + move
    if temp >= 8*4 and temp < 8*5:
        strip[temp] = (255,0,0)
    temp = 8*5+2 + move
    if temp >= 8*5 and temp < 8*6:
        strip[temp] = (255,0,0)
    temp = 8*6+2 + move
    if temp >= 8*6 and temp < 8*7:
        strip[temp] = (255,0,0)
    temp = 8*7+2 + move
    if temp >= 8*7 and temp < 8*8:
        strip[temp] = (255,0,0)


    temp = 8*1+5 + move
    if temp >= 8*1 and temp < 8*2:
        strip[temp] = (255,0,0)
    temp = 8*2+5 + move
    if temp >= 8*2 and temp < 8*3:
        strip[temp] = (255,0,0)


    temp = 8*4+5 + move
    if temp >= 8*4 and temp < 8*5:
        strip[temp] = (255,0,0)
    temp = 8*5+5 + move
    if temp >= 8*5 and temp < 8*6:
        strip[temp] = (255,0,0)
    temp = 8*6+5 + move
    if temp >= 8*6 and temp < 8*7:
        strip[temp] = (255,0,0)



    strip.write()
    time.sleep(0.2)

    move = move - 1
    if move < -8:
        move = 8