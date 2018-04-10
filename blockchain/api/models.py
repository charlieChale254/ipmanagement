from datetime import datetime

from blockchain.routes import db
from argon2 import PasswordHasher

from flask_login import UserMixin



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def hash_password(password: str):
        ph = PasswordHasher()
        hash = ph.hash(password)
        return hash

    def check_password(self, password):
        ph = PasswordHasher()
        return ph.verify(self.password_hash, password)


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(64))
    body = db.Column(db.String(120))

    def __repr__(self):
        return '<Property {}>'.format(self.token)



