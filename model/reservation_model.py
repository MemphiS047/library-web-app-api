from DB.alchemy_setup import ORM, engine
from sqlalchemy import Column, DateTime, Integer, String, select
from sqlalchemy.orm import Session

Base = ORM()
engine = engine() 

class ReservationModel(Base):

    __tablename__ = 'reservation'

    def __init__(self, reserve_id, room_id, reservedBy, length, start_time, end_time):
        self.reserve_id = reserve_id
        self.room_id = room_id
        self.reservedBy = reservedBy
        self.length = length
        self.start_time = start_time
        self.end_time = end_time

    def create_reservation(self):
        pass

    def cancel_reservation(self):
        pass

    @classmethod
    def get_reservation_by_date(cls):
        pass

    @classmethod
    def is_reserved(cls):
        pass