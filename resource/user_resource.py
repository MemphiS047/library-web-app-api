from flask_restful import Resource, reqparse
from model.user_model import UserModel


class UserAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('firstname',type=str)
    parser.add_argument('lastname',type=str)
    parser.add_argument('faculty',type=str)
    parser.add_argument('department',type=str)
    parser.add_argument('username', type=str)
    parser.add_argument('is_admin', type=str)
    parser.add_argument('password', type=str)
    
    def post(self):
        data = UserAPI.parser.parse_args()
        user = UserModel(data['firstname'],data['lastname'],data['faculty'],data['department'],
        data['username'],data['is_admin'],data['password'])
        result = UserModel.get_user_email(user.username)
        if(result):
            return {"message": "Account with that email already exists"}, 400
        else:
            user.addUser()
            return {"message": "User created successfully"}, 201

class AuthAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str)
    parser.add_argument('password', type=str)
    
    def get(self):
        body = AuthAPI.parser.parse_args()
        result = UserModel.get_user_email(body["username"])
        if(result):
            return {"message": "Authentication successful"}, 201
        else:
            return {"message": "Couldn't find any user with these credentials"}, 400
