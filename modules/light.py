#!/usr/bin/python
import time
from RPi.GPIO import GPIO

def get():
    LIGHT_INPUT_PIN = 38
    LIGHT_OUTPUT_PIN = 22

    count = 0

    #Output on the pin for 
    GPIO.setup(LIGHT_OUTPUT_PIN, GPIO.OUT)
    GPIO.output(LIGHT_OUTPUT_PIN, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(LIGHT_OUTPUT_PIN, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(LIGHT_OUTPUT_PIN) == GPIO.LOW):
        count += 1

    return count
