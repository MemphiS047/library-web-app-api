from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session, relationship
from sqlalchemy import select
from sqlalchemy.sql.schema import ForeignKey
""" import model.user_model as user_model, model.room_model as room_model """
from DB.alchemy_setup import ORM, engine
import model.room_model as room_model
from datetime import datetime, timedelta
Base = ORM()
engine = engine() 

""" 
+------------+-------------------+------+-----+---------+------------------+
| Field      | Type              | Null | Key | Default | Extra            |
+------------+-------------------+------+-----+---------+------------------+
| reserve_id | int unsigned      | NO   | PRI | NULL    | auto_increment   |
| room_id    | int unsigned      | NO   | MUL | NULL    |                  |
| reservedBy | int unsigned      | NO   | MUL | NULL    |                  |
| length     | enum('1','2','3') | NO   |     | 1       |                  |
| start_time | datetime          | NO   |     | NULL    |                  |
| end_time   | datetime          | YES  |     | NULL    | STORED GENERATED |
+------------+-------------------+------+-----+---------+------------------+
"""

class reserveRoomModel(Base):

    __tablename__ = 'room_reservations'

    reserve_id          = Column(Integer, primary_key=True)
    room_id             = Column(Integer)#ForeignKey(room_model.RoomModel.room_id)
    reservedBy          = Column(Integer)# ForeignKey(user_model.UserModel.user_id)
    length              = Column(Integer)
    start_time          = Column(String)

    def __init__(self, reserve_id, room_id, reservedBy, length, start_time):
        self.reserve_id          = reserve_id
        self.room_id             = room_id
        self.reservedBy          = reservedBy
        self.length              = length
        self.start_time          = start_time

    def reserve_room(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    @classmethod
    def get_rooms(cls, selectDay):
        date = "{}".format(selectDay)
        print("RECEIVED DATE FROM URL", date)
        date_time_obj = datetime.strptime(date, '%Y-%m-%d')
        date_time_obj_1day = date_time_obj + timedelta(days=1)
        reservedHours = Session(engine).execute(select(cls.room_id, cls.start_time).where(cls.start_time.between(date_time_obj, date_time_obj_1day)))
        return reservedHours
    
#select start_time, SUBSTRING(start_time,12,2) from room_reservations where start_time between "2021-12-13" and "2021-12-14";