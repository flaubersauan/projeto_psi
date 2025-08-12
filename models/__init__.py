from models import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, PrimaryKey = True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text, Unique = True)

    def __repr__(self):
        return f'<{self.id}>'
