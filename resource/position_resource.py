
import datetime

from flask import request
from flask_restful import Resource, reqparse
from model.position_model import PositionModel, JobApplicationModel

class PositionAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('job_id', type=int)
    parser.add_argument('job_title', type=str)
    parser.add_argument('Job_description', type=str)
    parser.add_argument('payment', type=int)
    parser.add_argument('job_type', type=str)
    parser.add_argument('user_id')
    parser.add_argument('respond', type=str)

    def get(self):
        data = PositionAPI.parser.parse_args()
        query = {
            "queryLst": [

            ]
        }
        jobApplicationUid, appliedJob = "N/A", "N/A"
        if("user_id" != ""):
            result_1 = JobApplicationModel.get_job_application_by_user_id(data["user_id"])
            if(result_1 != None):
                jobApplicationUid = result_1.user_id
                appliedJob = result_1.job_id
        print("RECIEVED DATA", jobApplicationUid, appliedJob)
        result_2 = PositionModel.get_all_positions()
        for row in result_2:
            query["queryLst"].append({
                "job_id":row["job_id"],
                "job_title":row["job_title"],
                "Job_description":row["Job_description"],
                "payment":row["payment"],
                "job_type":row["job_type"],
                "jobApplicationUid": jobApplicationUid,
                "appliedJob": appliedJob
            })
        return query, 201, {'Access-Control-Allow-Origin': '*'}

    def post(self):
        data = PositionAPI.parser.parse_args()
        position_model = PositionModel(data['job_title'], data['Job_description'], data['payment'], data['job_type'])
        position_model.create_position()
        return {"message" : "Position created successfully"} , 201
    
    def update(self):
        pass

    def delete(self):
        pass

class PositionManagmenetAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('job_id', type=int)
    parser.add_argument('user_id', type=int)
    parser.add_argument('respond', type=str)

    def post(self):
        data = PositionAPI.parser.parse_args()
        print("DATA", data)
        job_application = JobApplicationModel(data["job_id"], data["user_id"], data["respond"])
        job_application.create_application()
        return {"message" : "Successfully created application"}, 201, {'Access-Control-Allow-Origin': '*'}
        