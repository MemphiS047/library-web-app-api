from DB.alchemy_setup import ORM, engine
from sqlalchemy import Column, DateTime, Integer, String, select
from sqlalchemy.orm import Session

Base = ORM()
engine = engine() 

class BookModel(Base):

    __tablename__ = 'books'

    book_id             = Column(Integer, primary_key=True) 
    book_name           = Column(String)
    author              = Column(String)
    prolog              = Column(String)
    Publisher           = Column(String)
    Language            = Column(String)
    Publication_Date    = Column(DateTime)
    numberOFPages       = Column(Integer)
    Dimensions          = Column(String)
    editionNumber       = Column(Integer)
    is_available        = Column(Integer)

    def __init__(self, book_name, author, Publisher, Language, numberOFPages, is_available):
        self.book_name          = book_name
        self.author             = author
        self.prolog             = None
        self.Publisher          = Publisher
        self.Language           = Language
        self.Publication_Date   = None
        self.numberOFPages      = numberOFPages
        self.Dimensions         = None
        self.editionNumber      = None
        self.is_available       = is_available

    def create_book(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    def update_status(self):
        new_status = 1 # By defualt 1 
        if(self.is_available == 0):
            new_status = 1
        else:
            new_status = 0
        with Session(engine) as session:
            session.query(self.__class__).filter(self.__class__.book_id == self.book_id).update({'is_available': new_status})
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
    
    @classmethod
    def get_book_by_id(cls, book_id):
        with Session(engine) as session:
            result = session.query(cls).filter_by(book_id=book_id).first()
            return result
