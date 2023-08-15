from flask import request, jsonify, make_response
from flask_restx import Resource 
from models import User, signup_model, login_model ,auth_ns
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

@auth_ns.route('/signup')
class SignUp(Resource):
    @auth_ns.expect(signup_model)
    def post(self):
        data=request.get_json()
        
        username = data.get('username')
        db_user=User.query.filter_by(username=username).first()

        if db_user is not None:
            return jsonify({"message":f"User with username {username} already exist"})

        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password'))
        )

        new_user.save()
        return make_response(jsonify({"message": "User created successfuly"}), 201)
    
@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')
    
        db_user = User.query.filter_by(username=username).first()
        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.username)
            refresh_token = create_refresh_token(identity=db_user.username)

            return jsonify({"access_token": access_token, "refresh_token": refresh_token})
