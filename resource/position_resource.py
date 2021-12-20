
import datetime

from flask import request
from flask_restful import Resource, reqparse
from model.position_model import PositionModel

class PositionAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('job_id', type=int)
    parser.add_argument('job_title', type=str)
    parser.add_argument('Job_description', type=str)
    parser.add_argument('payment', type=int)
    parser.add_argument('job_type ', type=str)


    def post(self):
        data = request.get_json()

    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        query = {
            "queryLst": [

            ]
        }
        result = PositionModel.get_all_positions()
        for row in result:
            query["queryLst"].append({
                "job_id":row["job_id"],
                "job_title":row["job_title"],
                "Job_description":row["Job_description"],
                "payment":row["payment"],
                "job_type":row["job_type"]
            })
        return query, 201, {'Access-Control-Allow-Origin': '*'}

        