import datetime
from re import search
from flask_restful import Resource, reqparse
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session

from model.book_model import BookModel

class BookAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('book_id', type=int)
    parser.add_argument('book_name', type=str)
    parser.add_argument('prolog', type=str)
    parser.add_argument('Publisher', type=int)
    parser.add_argument('Language', type=str)
    parser.add_argument('Publication_Date', type=datetime)
    parser.add_argument('numberOFPages', type=int)
    parser.add_argument('Dimensions', type=str)
    parser.add_argument('editionNumber', type=str)
    parser.add_argument('translator', type=int)


    def post(self):
        data = BookAPI.parser.parse_args()
        book = BookModel(data['book_id'], data['book_name'], data['prolog'], 
                            data['Publisher'], data['Language'], 
                            data['Publication_Date'], data['numberOFPages'],
                            data['Dimensions'], data['editionNumber'], data['translator'])
        book.create_book()
        return {"message":"Book created successfully"}, 201


    def get(self):
        search_string = "asda"
        temp = BookModel.get_search_result(search_string)
        print(temp)
        return {
            "message":"successfull"
        }