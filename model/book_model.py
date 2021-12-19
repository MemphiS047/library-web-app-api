from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from sqlalchemy import select

from DB.alchemy_setup import ORM, engine

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
    translator          = Column(String)

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
    
    def delete_book(self):
        pass

    
    def update_book(self):
        pass

    @classmethod
    def get_search_result(cls, search_string):
        search = "%{}%".format(search_string)
        with Session(engine) as session:
            # result_book = session.execute(select(cls).where(cls.book_name.like(search)))
            result = session.execute(select(cls).where(cls.author.like(search) & cls.book_name.like(search)))
            for row in result:
                print(row[0].book_name)
                print(row[0].author)