from sqlalchemy.ext.declarative import declarative_base

def ORM():
    Base = declarative_base()
    print(f"Declarative base class - {Base}")
    return Base