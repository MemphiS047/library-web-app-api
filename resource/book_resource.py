import datetime

from flask import request
from flask_restful import Resource, reqparse
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
        result = BookModel.get_search_result(search_string)
        for row in result:
            query["queryLst"].append({
                "bookId":f"{row[0].book_id}",
                "bookName":f"{row[0].book_name}",
                "authorName":f"{row[0].author}"
                });
        return query, 201, {'Access-Control-Allow-Origin': '*'}

class BorrowAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('bookId', type=int)
    parser.add_argumetn('userId', type=str)


    def post(self):
        borrowed_date = datetime.now()
        data = BorrowAPI.parser.parse_args()
        
        bookId = data["bookId"]
        userId = data["userId"]
        deadline = borrowed_date + datetime.timedelta(days=20)
        is_returned = False