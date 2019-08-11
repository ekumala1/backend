from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_dotenv import DotEnv
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

app = Flask(__name__)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
engine = db.create_engine(DATABASE_URL, {})
Session = sessionmaker(bind=engine)
session = Session()
