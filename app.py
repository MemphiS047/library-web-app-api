from re import S
from flask import Flask
from flask_restful import Api
from resource.book_resource import BookAPI


app = Flask(__name__)
api = Api(app)


api.add_resource(BookAPI, '/api/createbook', endpoint='Book1')
api.add_resource(BookAPI, '/api/getbook', endpoint='Book2')

if __name__ == "__main__":
    app.run(port=5000, debug=True)