
import time
import board
import digitalio

led0 = digitalio.DigitalInOut(led0)
led0.direction = digitalio.Direction.OUTPUT
led1 = digitalio.DigitalInOut(led1)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(led2)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(led3)
led3.direction = digitalio.Direction.OUTPUT

while True:
    led0.value = True
    time.sleep(1)
    led0.value = False
    time.sleep(1)
    led1.value = True
    time.sleep(1)
    led1.value = False
    time.sleep(1)
    led2.value = True
    time.sleep(1)
    led2.value = False
    time.sleep(1)
    led3.value = True
    time.sleep(1)
    led3.value = False
    time.sleep(1)

