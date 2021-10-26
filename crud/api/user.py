from flask import jsonify
from flask_restful import Resource, request
import bcrypt
from db.userRepository import *
from models.user import User


def checkDuplicate(self, email):
    if (findByEmail(email)):
        raise Exception('이미 존재하는 email입니다.')


def isExistUser(self, by_id):
    if by_id == None:
        raise Exception('해당 아이디가 존재하지 않습니다.')

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
        permit(User(0, email, password))
        return jsonify(result="success")

    """
    get all users
    """
    def get(self):
        a_ll = findALl()
        cnt = len(a_ll)
        data = [User(i[0], i[1]).json() for i in a_ll]
        return jsonify(result="success", count=cnt, data=data)


### http://localhost:5000/user/<int:param>
class UserApi2(Resource):
    '''
    delete by user id
    '''
    def delete(self, param):
        by_id = findById(param)
        try:
            isExistUser(by_id)
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        remove(param)
        return jsonify(result="success")
    '''
    find by user id
    '''
    def get(self, param):
        by_id = findById(param)
        try:
            isExistUser(by_id)
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        data=User(by_id[0], by_id[1]).json()
        return jsonify(result="success", data=data)


### http://localhost:5000/user/update
class UserApi3(Resource):
    '''
    update user
    jwt이용해서 아이디 조회로 변경 예쩡
    '''
    def post(self):
        email=request.json.get('email')
        by_email=findByEmail(email)
        user = User(by_email[0],by_email[1],by_email[2])
        user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

        update(user)
        return jsonify(result="success")