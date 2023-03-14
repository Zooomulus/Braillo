import machine
import time
from time import sleep

#Solenoid A: GP3
#Solenoid B: GP7
#Solenoid C: GP10
solenoid_pins = {"A": machine.Pin(3, machine.Pin.OUT),
                 "B": machine.Pin(7, machine.Pin.OUT),
                 "C": machine.Pin(10, machine.Pin.OUT)}

#Braille letters
braille_map = {"a": "100",
               "b": "110",
               "k": "101",
               "l": "111",
               "but": "110"
               "like": "111"
               "c": "100100",
               "d": "100110",
               "e": "100010",
               "f": "110100",
               "g": "110110",
               "h": "110010",
               "i": "010100",
               "j": "010110",
               "k": "101000",
               "m": "101100",
               "n": "101110",
               "o": "101010",
               "p": "111100",
               "q": "111110",
               "r": "111010",
               "s": "011100",
               "t": "011110",
               "u": "101001",
               "v": "111001",
               "w": "010111",
               "x": "101101",
               "y": "101111",
               "z": "101011",
               " ": "000000",
               }

#text to braille
def text_to_braille(text):
    braille = ""
    for char in text:
        if char.lower() in braille_map:
            braille += braille_map[char.lower()]
    return braille

#activate solenoids using text func above
def activate_solenoids(braille):
    for i in range(len(braille)):
        if braille[i] == "1":
            if i == 0:
                solenoid_pins["A"].on()
            elif i == 1:
                solenoid_pins["B"].on()
            elif i == 2:
                solenoid_pins["C"].on()
        else:
            if i == 0:
                solenoid_pins["A"].off()
            elif i == 1:
                solenoid_pins["B"].off()
            elif i == 2:
                solenoid_pins["C"].off()

#Text input loop
while True:
    input_text = input("Enter text to convert to Braille: ")
    if not input_text:
        break
    braille_code = text_to_braille(input_text)

#definition
activate_solenoids(braille_code)

#delay
time.sleep(1)

#turn off
for pin in solenoid_pins.values():
    pin.off()
