#!/usr/bin/python
import sys, os, sqlite3, atexit
sys.path.append(os.path.curdir)

from RPi import GPIO
from flask import Flask
from config import config_handler as cfg
from config import db_handler

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    db_handler.init()
    app.run(debug=True, port=80, host='0.0.0.0')
    print "service started"

@atexit.register
def stop():
    GPIO.cleanup()
    print "service stopped"