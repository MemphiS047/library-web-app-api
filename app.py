from resource.announcement_resource import AnnouncementAPI
from resource.book_resource import BookAPI
from resource.position_resource import PositionAPI

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(BookAPI, '/api/managebooks')
api.add_resource(PositionAPI, '/api/managepositions')
api.add_resource(AnnouncementAPI, '/api/manageannouncements')

app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    cors = CORS(app)
    app.run(port=5000, debug=True)
