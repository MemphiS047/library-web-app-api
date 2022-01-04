from DB.alchemy_setup import ORM, engine
from sqlalchemy import Column, DateTime, Integer, String, select
from sqlalchemy.orm import Session
import enum
Base = ORM()
engine = engine() 



class BorrowModel(Base):

    __tablename__ = 'book_reservations'

    reservation_id      = Column(Integer, primary_key=True)
    book_id             = Column(Integer)
    reserv_datetime     = Column(String)
    duration            = Column(Integer)
    user_id             = Column(Integer)
    is_returned         = Column(Integer)

    def __init__(self, reservation_id, book_id, reserv_datetime, duration, user_id, is_returned):
        self.reservation_id      = reservation_id
        self.book_id             = book_id
        self.reserv_datetime     = reserv_datetime
        self.duration            = duration
        self.user_id             = user_id
        self.is_returned         = is_returned

    def create_borrow_request(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    def update_borrow(self):
        pass

    def delete_borrow(self):
        with Session(engine) as session:
            session.delete(self)
            session.commit()