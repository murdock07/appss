from modules import *

def start():
    load_config()
    GPIO.setmode(GPIO.BOARD)
    print "service started"

def stop():
    GPIO.cleanup()
    print "service stopped"

def load_config():
    print "config loaded"