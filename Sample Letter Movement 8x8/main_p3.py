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
    temp = 8*x+8 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)



    x = 1
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+8 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)



    x = 2
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+8 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)


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
    temp = 8*x+8 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)



    x = 4
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+8 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)



    x = 5
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+8 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)


    # line 6, lights 2,5 (starting on screen)
    # line 6, lights 8 (starting off screen)
    x = 6
    temp = 8*x+2 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+5 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)
    temp = 8*x+8 + move
    if temp >= 8*x and temp < 8*(x+1):
        strip[temp] = (255,0,0)



    # line 7, lights 2,3,4 (starting on screen)
    # line 7, lights 8,9,10,11 (starting off screen)
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


    for i in range (8,12):
        temp = 8*x+i + move
        if temp >= 8*x and temp < 8*(x+1):
            strip[temp] = (255,0,0)

    strip.write()
    time.sleep(0.2)

    move = move - 1
    if move < -12:
        move = 8