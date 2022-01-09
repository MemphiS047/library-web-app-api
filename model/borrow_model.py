from DB.alchemy_setup import ORM, engine
from sqlalchemy import Column, DateTime, Integer, String, select, ForeignKey
from sqlalchemy.orm import Session
import enum
from .user_model import UserModel
Base = ORM()
engine = engine() 



class BorrowModel(Base):

    __tablename__ = 'book_reservations'

    reservation_id      = Column(Integer, primary_key=True)
    book_id             = Column(Integer)
    reserv_datetime     = Column(String)
    duration            = Column(Integer)
    user_id             = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    is_returned         = Column(Integer)

    def __init__(self, book_id, reserv_datetime, duration, user_id, is_returned):
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
    
    @classmethod
    def get_borrow_record_by_id(cls, reservation_id):
        with Session(engine) as session:
            result = session.query(cls).filter_by(reservation_id=reservation_id).first()
            return result

    @classmethod
    def get_all_borrow_status_by_username(cls, username):
        result = Session(engine).query(cls, UserModel).join(UserModel, UserModel.user_id == cls.user_id).filter(UserModel.username == username)
        return result