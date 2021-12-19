from re import S
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resource.book_resource import BookAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(BookAPI, '/api/createbook', endpoint='Book1')
api.add_resource(BookAPI, '/api/getbook', endpoint='Book2')

app.config['CORS_HEADERS'] = 'Content-Type'

# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Autherization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response

if __name__ == "__main__":
    cors = CORS(app)
    app.run(port=5000, debug=True)