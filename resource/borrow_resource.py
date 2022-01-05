import datetime

from flask import request
from flask_restful import Resource, reqparse
from model.borrow_model import BorrowModel
from flask_restful import inputs
from model.book_model import BookModel
from model.user_model import UserModel

class BorrowAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('book_id', type=int)
    parser.add_argument('reserv_datetime', type=str)
    parser.add_argument('duration', type=int)
    parser.add_argument('user_id', type=int)
    parser.add_argument('is_returned', type=int)
  
    def post(self):
        data = BorrowAPI.parser.parse_args()
        borrow_req = BorrowModel(data['book_id'], data['reserv_datetime'], data['duration'], data['user_id'], data['is_returned'])
        book_model = BookModel.get_book_by_id(data['book_id'])
        borrow_req.create_borrow_request()
        book_model.update_status()
        return {"message" : "Borrow request created successfully"}, 201, {'Access-Control-Allow-Origin': '*'}

    def update(self):
        pass

    def delete(self):
        pass
    
    def get(self):
        query = {
            "queryLst" : [

            ]
        }
        result = BorrowModel.get_all_borrow_status()
        for row in result:
            user = UserModel.get_user_by_id(row["user_id"])
            book = BookModel.get_book_by_id(row["book_id"])
            query["queryLst"].append({
                "book_id" : row["book_id"],
                "reserv_datetime": str(row["reserv_datetime"]),
                "duration": row["duration"],
                "user_id": row["user_id"],
                "is_returned": row["is_returned"],
                "firstname": user.firstname,
                "bookname": book.book_name,
            })
        return query, 201, {'Access-Control-Allow-Origin': '*'}

