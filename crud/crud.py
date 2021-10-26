from flask_restful import Api
from flask import Flask
from config import Config
from utils import routes

app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = Config.JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = Config.JWT_REFRESH_TOKEN_EXPIRES
api = Api(app)

routes.init_routes(api)

if __name__ == "__main__":
    app.run(debug=True)