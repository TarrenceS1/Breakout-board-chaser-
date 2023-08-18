import time
import board
import digitalio

red_led = digitalio.DigitalInOut(board.GP13)
red_led.direction = digitalio.Direction.OUTPUT
amber_led = digitalio.DigitalInOut(board.GP10)
amber_led.direction = digitalio.Direction.OUTPUT
green_led = digitalio.DigitalInOut(board.GP7)
green_led.direction = digitalio.Direction.OUTPUT

while True:
    `
    time.sleep(1)
    green_led.value = True
    time.sleep(1)
    green_led.value = False
    time.sleep(1)
    amber_led.value =True
    time.sleep(1)
    amber_led.value = False
    time.sleep(1)
    red_led.value = True
    time.sleep(1)
    red_led.value = False
