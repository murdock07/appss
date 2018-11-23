from flask import Flask
from modules import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

def start():
    load_config()
    GPIO.setmode(GPIO.BOARD)
    print "service started"

def stop():
    GPIO.cleanup()
    print "service stopped"

def load_config():
    print "config loaded"