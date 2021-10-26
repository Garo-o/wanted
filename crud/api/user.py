from flask import jsonify
from flask_restful import Resource, request
import bcrypt
from db.userRepository import *
from models.user import User
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from utils import role

def checkDuplicate(email):
    if (findByEmail(email)):
        raise Exception('이미 존재하는 email입니다.')


def isExistUser(by_id):
    if by_id == None:
        raise Exception('해당 아이디가 존재하지 않습니다.')

def isAdmin(jwt):
    roles = jwt['roles'].split(',')
    flag = False
    for r in roles:
        if r == role.ROLE_ADMIN:
            flag = True
    if not flag:
        raise Exception('권한이 없습니다.')


def isMe(email):
    if not get_jwt_identity() == email:
        raise Exception('권한이 없습니다.')


### http://localhost:5000/user
class UserApi1(Resource):
    """
    sign up
    """
    def post(self):
        email = request.json.get('email')
        try:
            checkDuplicate(email)
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])
        password = request.json.get('password')
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        permit(User(0, email, ["ROLE_USER"], password))
        return jsonify(result="success")

    '''
    get all users
    @ADMIN
    '''
    @jwt_required()
    def get(self):
        try:
            isAdmin(get_jwt())
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        a_ll = findALl()
        cnt = len(a_ll)
        data = [User(i[0], i[1], i[2].split(",")).json2() for i in a_ll]
        return jsonify(result="success", count=cnt, data=data)


### http://localhost:5000/user/<int:param>
class UserApi2(Resource):
    '''
    delete by user id
    @ADMIN, USER
    '''
    @jwt_required()
    def delete(self, param):
        by_id = findById(param)
        try:
            isExistUser(by_id)
            isAdmin(get_jwt())
            isMe(by_id[1])
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        remove(param)
        return jsonify(result="success")
    '''
    find by user id
    @ADMIN, USER
    '''
    @jwt_required()
    def get(self, param):
        by_id = findById(param)
        try:
            isExistUser(by_id)
            isAdmin(get_jwt())
            isMe(by_id[1])
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        data = User(by_id[0], by_id[1], by_id[2].split(",")).json2()
        return jsonify(result="success", data=data)


### http://localhost:5000/user/update
class UserApi3(Resource):
    '''
    update user
    @USER
    '''
    @jwt_required()
    def post(self):
        email = get_jwt_identity()
        by_email = findByEmail(email)
        password = request.json.get('password')
        user = User(by_email[0], by_email[1], by_email[2], by_email[3])
        user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        update(user)
        return jsonify(result="success")