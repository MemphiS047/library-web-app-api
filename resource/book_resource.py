import datetime
from re import search

from flask import request
from flask_restful import Resource, reqparse
from model.book_model import BookModel
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import Session


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
        search_string = request.args.get('search_string')
        query = {
            "queryLst" : []
        }
        result = BookModel.get_search_result(search_string)
        for row in result:
            query["queryLst"].append({
                "book_id":f"{row[0].book_id}",
                "book_name":f"{row[0].book_name}",
                "author":f"{row[0].author}"
                });
        return query, 201, {'Access-Control-Allow-Origin': '*'}
