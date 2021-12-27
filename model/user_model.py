from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session, backref, relationship
from sqlalchemy import select
from sqlalchemy.sql.expression import false, true
import enum
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BOOLEAN, VARCHAR, Boolean, Enum

from DB.alchemy_setup import ORM, engine

Base = ORM()
engine = engine()

class UserModel(Base):

    class myEnum(enum.Enum):
        false = 0
        true = 1

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    faculty = Column(String)
    department = Column(String)
    username = Column(VARCHAR, primary_key=True)
    is_admin = Column(Enum(myEnum))
    password = Column(VARCHAR)

    def __init__(self, firstname, lastname, faculty, department, username, is_admin, password):
        self.firstname = firstname
        self.lastname = lastname
        self.faculty = faculty
        self.department = department
        self.username = username
        self.is_admin = is_admin
        self.password = password

    def addUser(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()
            return False
    
    @classmethod
    def get_user_email(cls, username):
        with Session(engine) as session:
            result = session.query(cls).filter_by(username = username).first()
            return result