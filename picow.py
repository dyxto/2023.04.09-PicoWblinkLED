print("Hello Pico")

from machine import Pin
import utime
led = machine.Pin("LED", machine.Pin.OUT)

count=10

while count > 0:
    led.toggle()
    print("Toggle {}".format(count))
    count=count-1
    utime.sleep(.5)

'''
print("Hello Pico")

from machine import Pin
import utime
led = machine.Pin("LED", machine.Pin.OUT)

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
'''