from flask import jsonify
from flask_restful import Resource, request
from db.boardRepository import *
from models.board import Board
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from utils import role


def isExistBoard(by_id):
    if by_id == None:
        raise Exception('해당 게시글이 존재하지 않습니다.')


def isAdmin(jwt):
    roles = jwt['roles'].split(',')
    flag = False
    for r in roles:
        if r == role.ROLE_ADMIN:
            flag = True
    if not flag:
        raise Exception('권한이 없습니다.')


def isMe(email):
    if not get_jwt_identity() ==email:
        raise Exception('권한이 없습니다.')

### http://localhost:5000/board
class BoardApi1(Resource):
    '''
    new board
    @USER, ADMIN
    '''
    @jwt_required()
    def post(self):
        title = request.json.get('title')
        context = request.json.get('context')
        writer = get_jwt_identity()

        permit(Board(0, title, context, writer, '', 0))
        return jsonify(result="success")

    """
    get all boards list
    """
    def get(self):
        a_ll = findALl()
        cnt = len(a_ll)
        data = [Board(i[0], i[1], i[2], i[3], i[4], i[5]).json2() for i in a_ll]
        return jsonify(result="success", count=cnt, data=data)

### http://localhost:5000/board/<int:param>
class BoardApi2(Resource):
    '''
    delete by board id
    @ADMIN, USER
    '''
    @jwt_required()
    def delete(self, param):
        by_id = findById(param)
        try:
            isExistBoard(by_id)
            isAdmin(get_jwt())
            isMe(by_id[3])
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        remove(param)
        return jsonify(result="success")

    '''
    find boards list from (param-1)*limit , limit=5
    '''

    def get(self, param):
        limit = 5
        offset = param-1
        boards = findByOffsetWithLimit(offset, limit)
        cnt = len(boards)
        data = [Board(i[0], i[1], i[2], i[3], i[4], i[5]).json2() for i in boards]
        return jsonify(result="success", count=cnt, data=data)

    '''
    update board
    @USER
    '''
    @jwt_required()
    def post(self, param):
        board_ = findById(param)
        try:
            isExistBoard(board_)
            isMe(board_[3])
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        title = request.json.get('title')
        context = request.json.get('context')

        update(Board(param, title, context, '', '', 0))
        return jsonify(result="success")


### http://localhost:5000/board/get/<int:param>
class BoardApi3(Resource):
    '''
    find one by id
    '''
    def get(self, param):
        one = findById(param)
        try:
            isExistBoard(one)
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        data = Board(one[0], one[1], one[2], one[3], one[4], one[5]).json()
        return jsonify(result="success", data=data)
