# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
 
import board
import neopixel
 
pixpin = board.D0
numpix = 64

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set brightness to a high value.  1.0 is the maximum value, 0.0 is the lowest
    strip.brightness = 0.1
    
    # All the dots moving in a single row
    # All these dots are in row 0
    strip[2] = (255,0,0)
    strip[3] = (255,0,0)
    strip[4] = (255,0,0)

    # All these dots are in row 3
    strip[8*3+3] = (255,0,0)
    strip[8*3+4] = (255,0,0)

    # All these dots are in row 7
    strip[8*7+3] = (255,0,0)
    strip[8*7+4] = (255,0,0)




    # All the dots moving in a column arrangement
    # All these dots are in column 2
    strip[8*1+2] = (255,0,0)
    strip[8*2+2] = (255,0,0)
    strip[8*3+2] = (255,0,0)
    strip[8*4+2] = (255,0,0)
    strip[8*5+2] = (255,0,0)
    strip[8*6+2] = (255,0,0)
    strip[8*7+2] = (255,0,0)

    # All these dots are in column 5
    strip[8*1+5] = (255,0,0)
    strip[8*2+5] = (255,0,0)

    # All these dots are also in column 5, note row 3 is a gap
    strip[8*4+5] = (255,0,0)
    strip[8*5+5] = (255,0,0)
    strip[8*6+5] = (255,0,0)




    strip.write()