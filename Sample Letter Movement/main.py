# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
import board
import neopixel
 
pixpin = board.D0
numpix = 64

# modify maxlengthofadvertisement to the maximum lenght of pixels
maxlengthofadvertisement = 16
counttomaxlength = 0
i = 0

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


# modify the following table of RGB values
allrows = [[[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]]]
 
 
 
while True:

    strip.brightness = 0.1
    i = 0
    for r in range(0,8):
        for c in range(counttomaxlength,counttomaxlength+8):
            temp = c % maxlengthofadvertisement
            strip[i] = (allrows[r][temp][0],allrows[r][temp][1],allrows[r][temp][2])
            i += 1
    strip.write()
    time.sleep(0.2)


    counttomaxlength += 1
    if counttomaxlength > maxlengthofadvertisement:
        counttomaxlength = 0
