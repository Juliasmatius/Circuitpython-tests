import board
from digitalio import *
import time


button = DigitalInOut(board.GP1)
button.direction = Direction.INPUT
button.pull = Pull.UP

led_red = DigitalInOut(board.GP0)
led_red.direction = Direction.OUTPUT


led_ylw = DigitalInOut(board.GP16)
led_ylw.direction = Direction.OUTPUT


led_grn = DigitalInOut(board.GP3)
led_grn.direction = Direction.OUTPUT
i=0

while True:
    if not button.value:
        if i==0:
            led_grn.value=False
            led_ylw.value=False
            led_red.value=True
        elif i==1:
            led_grn.value=False
            led_ylw.value=True
            led_red.value=True
        elif i==2:
            led_grn.value=True
            led_ylw.value=False
            led_red.value=False
        elif i==3:
            led_grn.value=False
            led_ylw.value=True
            led_red.value=False
        elif i==4:
            led_grn.value=False
            led_ylw.value=False
            led_red.value=True
        elif i==5:
            led_red.value=False
            i=-1
        i+=1
        while not button.value:
            time.sleep(0.25)
    time.sleep(0.125)