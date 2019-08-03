from flask_restplus import Namespace, Resource, fields
from src import bcrypt

api = Namespace('register', description='Registration related operations')
parser = api.parser()

parser.add_argument('username', location='args')
parser.add_argument('password', location='args')
parser.add_argument('email', location='args')


@api.route('')
class RegisterUser(Resource):

    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        print(args)

        password = args['password']
        pwd_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        return {'password': pwd_hash}
