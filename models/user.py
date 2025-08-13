from flask_login import UserMixin
from .db import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Nome da tabela no banco
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    @staticmethod
    def get(user_id):
        return User.query.get(int(user_id))

    @staticmethod
    def all():
        return User.query.all()
