#double rotation 
from machine import Pin
import time

mag1 = (Pin(14, Pin.OUT))
mag2 = (Pin(25, Pin.OUT))
mag3 = (Pin(26, Pin.OUT))
mag4 = (Pin(27, Pin.OUT))


val= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

delay = 0.005
count1 = 0
while count1<250:
#for i in range (0, 1000, 1):
    for i in val:
        mag1.value(i[0])
        mag2.value(i[1])
        mag3.value(i[2])
        mag4.value(i[3])
        time.sleep(delay)
    count1 +=1
    print(count1)

