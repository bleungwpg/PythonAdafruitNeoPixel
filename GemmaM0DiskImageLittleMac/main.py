# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
 
import board
import neopixel
 
pixpin = board.D0
numpix = 64

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


list1 = [[0,0,0],[0,0,0],[253,253,84],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
         [0,0,0],[0,0,0],[253,253,84],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
         [65,249,218],[65,249,218],[65,249,218],[65,249,218],[65,249,218],[65,249,218],[65,249,218],[65,249,218],
         [0,0,0],[0,0,0],[253,253,84],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
         [0,0,0],[0,0,0],[253,253,84],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
         [0,0,0],[0,0,0],[253,253,84],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
         [249,65,243],[249,65,243],[249,65,243],[249,65,243],[249,65,243],[249,65,243],[249,65,243],[249,65,243],
         [0,0,0],[0,0,0],[253,253,84],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
 
 
 
while True:

    # set brightness to lowest visible.  0.0 would be no lights
    # fill the entire strip of lights with red. Yes, that means from 0 - 63
    # show for 1 second
    strip.brightness = 0.1
    strip.fill((255,0,0))
    strip.write()
    time.sleep(1)


    # set brightness to a high value.  1.0 is the maximum value
    # fill the first 3 lights with different colors. Note the first light is 0
    # show for 3 seconds
    strip.brightness = 0.7
    strip[0] = (255,0,0)
    strip[1] = (0,255,0)
    strip[2] = (0,0,255)
    for i in range(3,9):
        strip[i] = (0,0,0)
    strip[9] = (0,0,255)
    for i in range(10,numpix):
        strip[i] = (0,0,0)
    strip.write()
    time.sleep(3)
 
     # set brightness to medium value.
    # fill the certain rows and columns. You can make different lists for each sheet you want to use
    # show for 6 seconds
    strip.brightness = 0.3
    for i in range(0,numpix):
        strip[i] = (list1[i][0],list1[i][1],list1[i][2])
    strip.write()
    time.sleep(6)
