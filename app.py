from re import S
from flask import Flask
from flask_restful import Api, Resource
from sqlalchemy import select
from sqlalchemy import or_
app = Flask(__name__)
api = Api(app)

import datetime
from flask_restful import Resource, reqparse
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

def engine():
    connection_string="mysql://root:a1s2d3f4g5@localhost/medipolibdb"
    engine= create_engine(connection_string)
    return engine


def ORM():
    Base = declarative_base()
    print(f"Declarative base class - {Base}")
    return Base

Base = ORM()
engine = engine()

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

    @classmethod
    def get_search_result(cls, search_string):
        search = "%{}%".format(search_string)
        with Session(engine) as session:
            # result_book = session.execute(select(cls).where(cls.book_name.like(search)))
            result = session.execute(select(cls).where(cls.author.like(search) & cls.book_name.like(search)))
            for row in result:
                print(row[0].book_name)
                print(row[0].author)
class ManageBook(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('book_id', type=int)
    parser.add_argument('book_name', type=str)
    parser.add_argument('prolog', type=str)
    parser.add_argument('author', type=str)
    parser.add_argument('Publisher', type=str)
    parser.add_argument('Language', type=str)
    parser.add_argument('Publication_Date', type=str)
    parser.add_argument('numberOFPages', type=int)
    parser.add_argument('Dimensions', type=str)
    parser.add_argument('editionNumber', type=str)
    parser.add_argument('translator', type=str)

    def post(self):
        data = ManageBook.parser.parse_args()
        print("DATA -----------------")
        print(data)
        book = BookModel(data['book_id'], data['book_name'], data['prolog'], data['author'], data['Publisher'], data['Language'], data['Publication_Date'], data['numberOFPages'], data['Dimensions'], data['editionNumber'], data['translator'])

        book.create_book()
        return {"message":"Book created successfully"}, 201

    def get(self, search_string):
        temp = BookModel.get_search_result(search_string)
        print(temp)
        return {
            "message":"successfull"
        }

class GetBook(Resource):
    def get(self, search_string):
        print("!@#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        BookModel.get_search_result(search_string)
        return {
            "message":"successfull"
        }
# +------------------+--------------+------+-----+---------+----------------+
# | Field            | Type         | Null | Key | Default | Extra          |
# +------------------+--------------+------+-----+---------+----------------+
# | book_id          | int unsigned | NO   | PRI | NULL    | auto_increment |
# | book_name        | varchar(100) | NO   |     | NULL    |                |
# | author           | varchar(100) | NO   |     | NULL    |                |
# | prolog           | varchar(200) | YES  |     | NULL    |                |
# | Publisher        | varchar(50)  | NO   |     | NULL    |                |
# | Language         | varchar(10)  | NO   |     | NULL    |                |
# | Publication_Date | datetime     | YES  |     | NULL    |                |
# | numberOFPages    | int unsigned | YES  |     | NULL    |                |
# | Dimensions       | varchar(10)  | YES  |     | NULL    |                |
# | editionNumber    | int unsigned | YES  |     | NULL    |                |
# | translator       | varchar(50)  | YES  |     | NULL    |                |
# +------------------+--------------+------+-----+---------+----------------+

api.add_resource(ManageBook, '/createbook')
api.add_resource(GetBook, '/getbook/<string:search_string>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)