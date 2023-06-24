# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:01:18 2023

@author: YuuYuu
"""

#Creating a melody!

import pigpio
from time import sleep
 
BZ = 18
gpio = pigpio.pi()
gpio.set_mode(BZ, pigpio.OUTPUT)
 
scale = {
    "do": 523,
    "re": 587,
    "mi": 659,
    "fa": 698,
    "so": 783,
    "ra": 880,
    "si": 987,
    "dd": 1046,
    "rr":1147,
    "mm":1318,
    "ff":1397,
    "ss":1567
}
 
def melody(note, time):
    frequency = scale.get(note)
    if frequency:
        gpio.hardware_PWM(BZ, frequency, 500000)
        sleep(time)
        gpio.hardware_PWM(BZ, 0, 0)

notes=["do","re","mi","fa","so","ra","si","dd","rr","mm","ff","ss"]
def make_function(note):
    return lambda t: melody(note, t)

for note in notes:
    globals()[note] = make_function(note)
 
try:
    while True: 
        
        mi(0.2)   #【 マリオ 】音の長さがわからん
        sleep(0.05)
        mi(0.3)
        sleep(0.05)
        mi(0.3)
        sleep(0.2)
        do(0.2)
        sleep(0.05)
        mi(0.1)
        sleep(0.05)
        so(0.2)
        sleep(5) 
except KeyboardInterrupt:
    pass
finally:
    gpio.set_PWM_dutycycle(BZ,0)
    gpio.stop()
    
"""################################################################
For English-speaking users, 
please replace "do, re, mi, fa, so, ra, si" 
with "C, D, E, F, G, A, B" in the code.
################################################################"""
