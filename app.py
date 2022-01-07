from resource.announcement_resource import AnnouncementAPI
from resource.book_resource import BookAPI
from resource.position_resource import PositionAPI, PositionManagmenetAPI
from resource.borrow_resource import BorrowAPI
from resource.traffic_resource import TrafficAPI, TrafficCompAPI
from resource.reserve_room_resource import ReserveRoomAPI


from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resource.user_resource import UserAPI, AuthAPI

app = Flask(__name__)
api = Api(app)


api.add_resource(AuthAPI, '/api/auth')
api.add_resource(UserAPI, '/api/register')
api.add_resource(BookAPI, '/api/managebooks')
api.add_resource(PositionAPI, '/api/managepositions')
api.add_resource(PositionManagmenetAPI, '/api/apply')
api.add_resource(AnnouncementAPI, '/api/manageannouncements')
api.add_resource(BorrowAPI, '/api/borrow')
api.add_resource(TrafficAPI, '/api/traffic')
api.add_resource(TrafficCompAPI, '/api/trafficComp')
api.add_resource(ReserveRoomAPI, '/api/managereserveroom')

app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def add_header(response):
     response.headers['Access-Control-Allow-Origin'] = '*'
     response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
     response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE, OPTIONS, HEAD'
     response.headers['Access-Control-Expose-Headers'] = '*'
     return response

if __name__ == "__main__":
    # cors = CORS(app)
    app.run(port=5000, debug=True)