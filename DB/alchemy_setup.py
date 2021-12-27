from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

import configparser

config = configparser.ConfigParser()
config.read('setup.ini')

def ORM():
    Base = declarative_base()
    print(f"Initializing declerative base class - {Base}")
    return Base


def engine():
    DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}?auth_plugin=mysql_native_password'.format(
        user = config['DB']['user'],
        password = config['DB']['password'],
        server = config['DB']['host'],
        database = config['DB']['database'])
    print(DATABASE_URI)
    # connection_string="medipolibDB"
    engine= create_engine(DATABASE_URI)
    return engine

