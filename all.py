#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#Temperature sensor
TEMP_PIN_DATA = 32
#Light sensor
LIGHT_PIN_DATA = 22
#Sonar
SONAR_PIN_TRIG = 16
SONAR_PIN_ECHO = 18
#Relay
RELAY_PIN_IN1 = 36
RELAY_PIN_IN2 = 38

GPIO.setmode(GPIO.BOARD)

def setup_pins():
    GPIO.setup(SONAR_PIN_TRIG, GPIO.OUT)
    GPIO.setup(SONAR_PIN_ECHO, GPIO.IN)

def get_distance():
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
print "Distance:",distance,"cm"



GPIO.cleanup()