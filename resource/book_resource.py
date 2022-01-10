import datetime

from flask import request
from flask_restful import Resource, reqparse
from model.book_model import BookModel

class BookAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('book_name', type=str)
    parser.add_argument('prolog', type=str)
    parser.add_argument('Publisher', type=str)
    parser.add_argument('Language', type=str)
    parser.add_argument('Publication_Date', type=datetime)
    parser.add_argument('numberOFPages', type=int)
    parser.add_argument('Dimensions', type=str)
    parser.add_argument('editionNumber', type=int)
    parser.add_argument('is_available', type=int)
    parser.add_argument('author', type=str)


    def post(self):
        data = BookAPI.parser.parse_args()
        book = BookModel(data['book_name'], data['author'], data['Publisher'], data['Language'], data['numberOFPages'], 1)
        book.create_book()
        return {"message":"Book created successfully"}, 201

    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        search_string = request.args.get('search_string')
        query = {
            "queryLst" : [

            ]
        }
        value_of_is_available = False
        result = BookModel.get_search_result(search_string)
        for row in result:
            # if(row[0].is_available == 1):
            if(row[0].is_available == 1):
                value_of_is_available = True
            query["queryLst"].append({
                "bookId":f"{row[0].book_id}",
                "bookName":f"{row[0].book_name}",
                "authorName":f"{row[0].author}",
                "is_available": value_of_is_available
                });
            value_of_is_available = False
        return query, 201, {'Access-Control-Allow-Origin': '*'}