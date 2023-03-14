import machine
from machine import Pin
import time
from time import sleep


pin_solenoid_1 = machine.Pin(3, machine.Pin.OUT)  # GP3
pin_solenoid_2 = machine.Pin(7, machine.Pin.OUT)  # GP7
pin_solenoid_3 = machine.Pin(10, machine.Pin.OUT) # GP10

#pushing and pulling solenoids for 'a'
while True:
    pin_solenoid_1.value(1)
    time.sleep(3)
    pin_solenoid_1.value(0)
    pin_solenoid_1.value(1)
