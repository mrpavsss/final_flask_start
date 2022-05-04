from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import declarative_base
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import db

Base = declarative_base()

transaction_user = db.Table('transaction_user', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('transaction_id', db.Integer, db.ForeignKey('transactions.id'))
)

class Transaction(db.Model,SerializerMixin):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    AMOUNT = db.Column(db.FLOAT(), nullable=False, unique=False)
    TYPE = db.Column(db.String(6), nullable=False, unique=False)

    def __init__(self, AMOUNT, TYPE):
        self.AMOUNT = AMOUNT
        self.TYPE = TYPE

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    about = db.Column(db.String(300), nullable=True, unique=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column('registered_on', db.DateTime)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    is_admin = db.Column('is_admin', db.Boolean(), nullable=False, server_default='0')
    locations = db.relationship("Transaction",
                    secondary=transaction_user, backref="users")

    def __init__(self, email, password, is_admin):
        self.email = email
        self.password = password
        self.registered_on = datetime.utcnow()
        self.is_admin = is_admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.email