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
    # line 0, lights 2,3,4
    x = 0
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+3 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+4 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)


    # line 1, lights 2,5
    x = 1
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)


    # line 2, lights 2,5
    x = 2
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)


    # line 3, lights 2,3,4
    x = 3
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+3 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+4 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)


    # line 4, lights 2,5
    x = 4
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)


    # line 5, lights 2,5
    x = 5
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)


    # line 6, lights 2,5
    x = 6
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)



    # line 7, lights 2,3,4
    x = 7
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+3 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+4 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)






    strip.write()
    time.sleep(0.2)

    move = move - 1
    if move < -8:
        move = 8