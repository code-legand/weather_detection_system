# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 03:05:00 2023

@author: user
"""

import serial
import time

ser = serial.Serial("", 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Ready")

try:
    while True:
        time.sleep(0.01)
        if ser.inWaiting()>0:
            line = ser.readline().decode().strip()
            print(line)
except Exception:
    print("Device disconnected")
    ser.close()
