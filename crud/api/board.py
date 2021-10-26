from flask import jsonify
from flask_restful import Resource, request
from db.boardRepository import *
from models.board import Board


def isExistBoard(self, by_id):
    if by_id == None:
        raise Exception('해당 게시글이 존재하지 않습니다.')

### http://localhost:5000/board
class BoardApi1(Resource):
    '''
    new board
    '''
    def post(self):
        title = request.json.get('title')
        context = request.json.get('context')
        writer = request.json.get('writer')

        permit(Board(0, title, context, writer, '', ''))
        return jsonify(result="success")

    """
    get all boards
    """
    def get(self):
        a_ll = findALl()
        cnt = len(a_ll)
        data = [Board(i[0], i[1], i[2], i[3], i[4], i[5]).json() for i in a_ll]
        return jsonify(result="success", count=cnt, data=data)

### http://localhost:5000/board/<int:param>
class BoardApi2(Resource):
    '''
    delete by board id
    '''

    def delete(self, param):
        by_id = findById(param)
        try:
            isExistBoard(by_id)
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        remove(param)
        return jsonify(result="success")

    '''
    find limit boards from (param-1)*limit , limit=5
    '''

    def get(self, param):
        limit = 5
        offset = param-1
        boards = findByOffsetWithLimit(offset, limit)
        cnt = len(boards)
        data = [Board(i[0], i[1], i[2], i[3], i[4], i[5]).json() for i in boards]
        return jsonify(result="success", count=cnt, data=data)


### http://localhost:5000/board/update
class BoardApi3(Resource):

    '''
    update board
    '''

    def post(self):
        title = request.json.get('title')
        context = request.json.get('context')

        update(Board(0, title, context, '', '', ''))
        return jsonify(result="success")


### http://localhost:5000/board/get/<int:param>
class BoardApi4(Resource):
    '''
    delete by board id
    '''

    def get(self, param):
        one = findById(param)
        try:
            isExistBoard(one)
        except Exception as e:
            return jsonify(result="fail", error=e.args[0])

        data = Board(one[0], one[1], one[2], one[3], one[4], one[5]).json()
        return jsonify(result="success", data=data)
