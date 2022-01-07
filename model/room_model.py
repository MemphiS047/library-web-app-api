from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from sqlalchemy import select

from DB.alchemy_setup import ORM, engine

Base = ORM()
engine = engine()

""" 
+----------------+---------------+------+-----+---------+----------------+
| Field          | Type          | Null | Key | Default | Extra          |
+----------------+---------------+------+-----+---------+----------------+
| room_id        | int unsigned  | NO   | PRI | NULL    | auto_increment |
| room_name      | varchar(100)  | NO   | PRI | NULL    |                |
| capacity       | int unsigned  | NO   |     | NULL    |                |
| has_projection | enum('0','1') | NO   |     | 1       |                |
+----------------+---------------+------+-----+---------+----------------+
""" 

class RoomModel(Base):

    __tablename__ = 'meeting_rooms'

    room_id             = Column(Integer, primary_key=True) 
    room_name           = Column(String, primary_key=True)
    capacity            = Column(Integer)
    has_projection      = Column(String)

    def __init__(self, room_id, room_name, capacity, has_projection):
        self.room_id            = room_id
        self.room_name          = room_name
        self.capacity           = capacity
        self.has_projection     = has_projection


    def create_room(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()
    
    def delete_room(self):
        with Session(engine) as session:
            session.delete(self)
            session.commit()

    
    def update_rname(self, new_name):
        with Session(engine) as session:
            session.query(self.__class__).filter(self.__class__.room_name == self.room_name).update({'status': new_name})