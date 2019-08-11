from flask_restplus import Namespace, Resource, fields
from src import bcrypt, engine, session
from ..models import User

api = Namespace('login', description='Login related operations')
parser = api.parser()

parser.add_argument('username', location='args', default='daneolog')
parser.add_argument('password', location='args', default='password')
parser.add_argument('email', location='args', default='daneolog@gmail.com')


@api.route('')
class LoginUser(Resource):

    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        print(args)

        username = args.get('username')
        password = args.get('password')

        pwd_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        print(pwd_hash)
        users = session.query(User).filter(
            User.username == username, User.password == pwd_hash).all()

        print(users)

        if len(users) > 0:
            print(users)

        return {'response': 'success'}
