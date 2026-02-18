#push button direction change
from machine import Pin
import time

mag1 = (Pin(14, Pin.OUT))
mag2 = (Pin(25, Pin.OUT))
mag3 = (Pin(26, Pin.OUT))
mag4 = (Pin(27, Pin.OUT))
sw1 = Pin(4, Pin.IN, Pin.PULL_UP)
sw2 = Pin(21, Pin.IN, Pin.PULL_UP)

val= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

delay = 0.005

while True: 
    sw1value = sw1.value()
    sw2value = sw2.value()
    if(sw1value == 0):
        #while True :
            for i in val:
                mag1.value(i[0])
                mag2.value(i[1])
                mag3.value(i[2])
                mag4.value(i[3])
                time.sleep(delay)

    if(sw2value == 0):
        #while True:
            for i in reversed(val):
                mag1.value(i[0])
                mag2.value(i[1])
                mag3.value(i[2])
                mag4.value(i[3])
                time.sleep(delay)
                
    

