from api.user import *
from api.board import *
from api.auth import *

def init_routes(api):
    api.add_resource(AuthApi1, '/auth/login')
    api.add_resource(AuthApi2, '/auth/logout')

    api.add_resource(UserApi1, '/user')
    api.add_resource(UserApi2, '/user/<int:param>')
    api.add_resource(UserApi3, '/user/update')

    api.add_resource(BoardApi1, '/board')
    api.add_resource(BoardApi2, '/board/<int:param>')
    api.add_resource(BoardApi3, '/board/get/<int:param>')