import os
import configparser

def get(Key, Section):
    config = read_config()
    value = config[Section][Key]
    return value

def set(Key, Value, Section):
    config = read_config()
    config[Section][Key] = Value

    
def read_config():
    config = configparser.ConfigParser()
    pathToConfig = os.path.abspath('config/config.ini')
    config.read(pathToConfig)
    return config