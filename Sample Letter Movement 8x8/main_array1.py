# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
 
import board
import neopixel
 
pixpin = board.D0
numpix = 64

rotation = 0
i = 0

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


allrows = [[[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ]]]
 
 
 
while True:

    strip.brightness = 0.1
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            temp = (c + rotation) % 8
            strip[i] = (allrows[r][temp][0],allrows[r][temp][1],allrows[r][temp][2])
            i += 1
    strip.write()
    time.sleep(1)

    rotation += 1
    if rotation > 7:
        rotation = 0
