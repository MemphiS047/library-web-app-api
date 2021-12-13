# from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.orm import Session

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine

# def engine():
#     connection_string="mysql://root:a1s2d3f4g5@localhost/world"
#     engine= create_engine(connection_string)
#     return engine


# def ORM():
#     Base = declarative_base()
#     print(f"Declarative base class - {Base}")
#     return Base

# Base = ORM()
# engine = engine()

# class Book():
#     book_id, book_name, author, prolog, Publisher, Language, Publication_Date, numberOFPages, Dimensions, editionNumber, translator = None, None, None, None, None, None, None, None, None, None, None
#     def __init__(self, book_id, book_name, author, prolog, Publisher, Language, Publication_Date, numberOFPages, Dimensions, editionNumber, translator):
#         self.book_id            = book_id
#         self.book_name          = book_name
#         self.author             = author
#         self.prolog             = prolog
#         self.Publisher          = Publisher
#         self.Language           = Language
#         self.Publication_Date   = Publication_Date
#         self.numberOFPages      = numberOFPages
#         self.Dimensions         = Dimensions
#         self.editionNumber      = editionNumber
#         self.translator         = translator

# class BookModel(Base):

#     __tablename__ = 'books'

#     book_id             = Column(Integer, primary_key=True) 
#     book_name           = Column(String)
#     author              = Column(String)
#     prolog              = Column(String)
#     Publisher           = Column(String)
#     Language            = Column(String)
#     Publication_Date    = Column(DateTime)
#     numberOFPages       = Column(Integer)
#     Dimensions          = Column(String)
#     editionNumber       = Column(Integer)
#     translator          = Column(String)

#     def __init__(self, book_id, book_name, author, prolog, Publisher, Language, Publication_Date, numberOFPages, Dimensions, editionNumber, translator):
#         self.book_id            = book_id
#         self.book_name          = book_name
#         self.author             = author
#         self.prolog             = prolog
#         self.Publisher          = Publisher
#         self.Language           = Language
#         self.Publication_Date   = Publication_Date
#         self.numberOFPages      = numberOFPages
#         self.Dimensions         = Dimensions
#         self.editionNumber      = editionNumber
#         self.translator         = translator 

#     def create_book(self):
#         with Session(engine) as session:
#             session.add(self)
#             session.commit()

# # +------------------+--------------+------+-----+---------+----------------+
# # | Field            | Type         | Null | Key | Default | Extra          |
# # +------------------+--------------+------+-----+---------+----------------+
# # | book_id          | int unsigned | NO   | PRI | NULL    | auto_increment |
# # | book_name        | varchar(100) | NO   |     | NULL    |                |
# # | author           | varchar(100) | NO   |     | NULL    |                |
# # | prolog           | varchar(200) | YES  |     | NULL    |                |
# # | Publisher        | varchar(50)  | NO   |     | NULL    |                |
# # | Language         | varchar(10)  | NO   |     | NULL    |                |
# # | Publication_Date | datetime     | YES  |     | NULL    |                |
# # | numberOFPages    | int unsigned | YES  |     | NULL    |                |
# # | Dimensions       | varchar(10)  | YES  |     | NULL    |                |
# # | editionNumber    | int unsigned | YES  |     | NULL    |                |
# # | translator       | varchar(50)  | YES  |     | NULL    |                |
# # +------------------+--------------+------+-----+---------+----------------+