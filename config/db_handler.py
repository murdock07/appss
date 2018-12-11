import sys, os, sqlite3
sys.path.append(os.path.curdir)

from config import config_handler as cfg

def init():
    connection, cursor = connect()
    load_scheme(cursor)
    close(connection, cursor)

def connect():
    db_name = cfg.get('Name', 'Database')
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor

def close(connection, cursor):
    cursor.close()
    connection.close()

def load_scheme(cursor):
    db_schema = cfg.get('Schema', 'Database')    
    Schema = ''
    with open(db_schema, 'r') as File:
        Schema = File.read().replace('\n')
    sqlite3.complete_statement(Schema)
    cursor.executescript(Schema)