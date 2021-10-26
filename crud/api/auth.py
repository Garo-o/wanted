from flask_restful import Resource, request
from flask import jsonify
from db.userRepository import *
from flask_jwt_extended import get_jwt, create_access_token, jwt_required

import bcrypt

jwt_blacklist = set()


def checkUser(u, password):
    if len(u) == 0:
        raise Exception('존재하지 않는 유저입니다.')
    if not bcrypt.checkpw(password.encode('utf-8'), u[3]):
        raise Exception('Invalid email or password.')


class AuthApi1(Resource):
    """
    log in
    """
    def post(self):
        email = request.json.get("email")
        password = request.json.get("password")
        u = findByEmail(email)
        try:
            checkUser(u, password)
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])
        claims = {'roles': u[2]}
        access_token = create_access_token(identity=email, additional_claims=claims)

        return jsonify(result="success", token=access_token)

class AuthApi2(Resource):
    '''
    log out
    '''
    @jwt_required()
    def post(self):
        jwt_blacklist.add(get_jwt()['jti'])
        return jsonify(result="success")
