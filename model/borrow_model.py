from DB.alchemy_setup import ORM, engine
from sqlalchemy import Column, DateTime, Integer, String, select, Enum
from sqlalchemy.orm import Session
import enum
Base = ORM()
engine = engine() 


class BookModel(Base):

    class myEnum(enum.Enum):
        false = 0
        true = 1

    __tablename__ = 'book_reservations'

    reservation_id      = Column(Integer, primary_key=True)
    book_id             = Column(Integer)
    reserv_datetime     = Column(DateTime)
    duration            = Column(Integer)
    user_id             = Column(Integer)
    return_date         = Column(DateTime)
    is_returned         = Column(Enum(myEnum))

    def __init__(self, book_id, book_name, author, prolog, Publisher, Language, Publication_Date, numberOFPages, Dimensions, editionNumber, translator):
        self.book_id            = book_id
        self.book_name          = book_name
        self.author             = author
        self.prolog             = prolog
        self.Publisher          = Publisher
        self.Language           = Language
        self.Publication_Date   = Publication_Date
        self.numberOFPages      = numberOFPages
        self.Dimensions         = Dimensions
        self.editionNumber      = editionNumber
        self.translator         = translator 

    def create_book(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    def update_bookname(self, new_name):
        with Session(engine) as session:
            session.query(self.__class__).filter(self.__class__.name == self.name).update({'status': new_name})
            session.commit() 

    def delete_book(self):
        with Session(engine) as session:
            session.delete(self)
            session.commit()

    @classmethod
    def get_search_result(cls, search_string):
        search = "%{}%".format(search_string)
        result = Session(engine).execute(select(cls).where(cls.author.like(search) | cls.book_name.like(search)))
        return result
    
    