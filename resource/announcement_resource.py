import datetime

from flask import request
from flask_restful import Resource, reqparse
from model.announcement_model import AnnouncementModel

class AnnouncementAPI(Resource):
    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        query = {
            "queryLst" : [

            ]
        }
        result = AnnouncementModel.get_all_announcements()
        for row in result:
            print(row)
            query["queryLst"].append({
                "announce_id" : row["announce_id"],
                "announcement_title": row["announcement_title"],
                "announcer": row["announcer"],
                "message": row["message"],
                "announce_datetime": str(row["announce_datetime"]),
                "last_edit": row["last_edit"]
            })
        return query, 201, {'Access-Control-Allow-Origin': '*'}