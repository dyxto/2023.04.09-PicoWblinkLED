print("Hello Pico")

import machine
from machine import Pin
import utime
led = machine.Pin("LED", machine.Pin.OUT)

led.off()

count=5
while count > 0:
    led.toggle()
    print("LED ON {}".format(count))
    utime.sleep(.25)
    led.toggle()
    count=count-1
    utime.sleep(.25)
    
led.off()
print("LED OFF")