#!/usr/bin/python
import time
import RPi.GPIO as GPIO

def get():
    SONAR_PIN_TRIG = 16
    SONAR_PIN_ECHO = 18
    GPIO.output(SONAR_PIN_TRIG, GPIO.LOW)
    print "Waiting for sensor to settle"
    time.sleep(2)
    print "Calculating distance"

    pulse_start_time = time.time()
    GPIO.output(SONAR_PIN_TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(SONAR_PIN_TRIG, GPIO.LOW)

    while GPIO.input(SONAR_PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(SONAR_PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    return distance