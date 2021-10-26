from flask_restful import Api
from flask import Flask
from config import Config
from utils import routes
from flask_jwt_extended import JWTManager
from api.auth import jwt_blacklist

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in jwt_blacklist


routes.init_routes(api)

if __name__ == "__main__":
    app.run()
