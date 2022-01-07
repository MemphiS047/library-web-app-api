from datetime import datetime
from flask_restful import Resource, reqparse
from model.reserv_room_model import reserveRoomModel
from flask import request

class ReserveRoomAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('reserve_id',type=int)
    parser.add_argument('room_id',type=int)
    parser.add_argument('reservedBy',type=int)
    parser.add_argument('length',type=int)
    parser.add_argument('start_time', type=str)
    """ parser.add_argument('end_time', type=datetime) """
    
    def post(self):
        data = ReserveRoomAPI.parser.parse_args()
        reserve = reserveRoomModel(data['reserve_id'],data['room_id'],data['reservedBy'],data['length'],
        data['start_time'])
        reserve.reserve_room()
        return {"message": "Room reserved successfully"}, 201, {'Access-Control-Allow-Origin': '*'}

    def get(self):
        selectDay = request.args.get('selectDay')
        query = {
            "queryLst" : [

            ]
        }
        result = reserveRoomModel.get_rooms(selectDay)
        for row in result:
            query["queryLst"].append({
                "room_id":f"{row.room_id}",
                "start_time":f"{str(row.start_time)[11:13]}"
                });        
        print("QUERY", query)
        return query, 201, {'Access-Control-Allow-Origin': '*'}