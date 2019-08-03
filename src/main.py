from config import DATABASE_URL
from src import app
from flask_restplus import Api

api = Api(app)

from namespace.register import api as register_api
api.add_namespace(register_api)

if __name__ == '__main__':
    app.run(debug=True)
