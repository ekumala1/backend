from src import app
from flask_restplus import Api

api = Api(app)

from src.namespace.login import api as login_api
from src.namespace.register import api as register_api

api.add_namespace(login_api)
api.add_namespace(register_api)

if __name__ == '__main__':
    app.run(debug=True)
