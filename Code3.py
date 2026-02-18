#continuous bidirectional
from machine import Pin
import time

mag1 = (Pin(14, Pin.OUT))
mag2 = (Pin(25, Pin.OUT))
mag3 = (Pin(26, Pin.OUT))
mag4 = (Pin(27, Pin.OUT))

val= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
delay = 5
count1 = 0
count2 = 0
while True:
    while count1<250:
        for i in val :
            mag1.value(i[0])
            mag2.value(i[1])
            mag3.value(i[2])
            mag4.value(i[3])
            time.sleep_ms(delay)
        count1+=1
    while count2<250:
        for i in reversed(val) :
            mag1.value(i[0])
            mag2.value(i[1])
            mag3.value(i[2])
            mag4.value(i[3])
            time.sleep_ms(delay)
        count2+=1
    count1 = 0
    count2 = 0
            

