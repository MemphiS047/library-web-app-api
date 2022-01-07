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
    parser.add_argument('reservation_id', type=int)
  
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
        data = BorrowAPI.parser.parse_args()
        print("DATA $: ", data)
        BookModel.make_book_available(data["book_id"])
        borrow_record = BorrowModel.get_borrow_record_by_id(data["reservation_id"])
        borrow_record.delete_borrow()
        return {"message" : "Successfully deleted reservation record"}, 201
    
    def get(self):
        user_id = request.args.get('search_string')
        query = {
            "queryLst" : [

            ]
        }
        borrow_results = BorrowModel.get_all_borrow_status_by_user_id(user_id)
        user = UserModel.get_user_by_id(user_id)
        for borrow_row in borrow_results:
            book = BookModel.get_book_by_id(borrow_row["book_id"])
            query["queryLst"].append({
                "reservation_id" : borrow_row["reservation_id"],
                "book_id" : borrow_row["book_id"],
                "reserv_datetime": str(borrow_row["reserv_datetime"]),
                "duration": borrow_row["duration"],
                "user_id": borrow_row["user_id"],
                "is_returned": borrow_row["is_returned"],
                "firstname": user.firstname,
                "bookname": book.book_name,
                "author": book.author
            })
        return query, 201, {'Access-Control-Allow-Origin': '*'}

