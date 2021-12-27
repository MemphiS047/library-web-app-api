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
        result = UserModel.get_user_by_email(user.username)
        if(result):
            return {"message": "Account with that email already exists"}
        else:
            user.addUser()
            return {"message": "User created successfully"}, 201

class AuthAPI(Resource):
    par = reqparse.RequestParser()
    par.add_argument('username', type=str)
    par.add_argument('password', type=str)
    
    def post(self):
        body = AuthAPI.par.parse_args()
        result = UserModel.get_user_by_email(body["username"])
        if(result and (body["password"] == result.password and body["username"] == result.username)):
            return {"message": "Authentication successful",
            "credentials" : {
                "username" : result.username,
                "password" : result.password,
                "firstname" : result.firstname,
                "lastname" : result.lastname,
                }
            }, 201
        else:
            return {"message": "Couldn't find any user with these credentials"}