from models import configDB
from models.configDB import db
from helpers.sqlalchemy_mysql_binary_uuid import BinaryUUID
from uuid import uuid4


class Product(configDB.db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    id = db.Column('id', BinaryUUID, primary_key=True, default=uuid4)
    name = db.Column(db.String(70), unique=True)
    price = db.Column(db.String(100))

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Books(configDB.db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    author = db.Column(db.String(100))
    read=db.Column(db.Boolean)

    def __init__(self, title, author,read):
        self.title = title
        self.author = author
        self.read=read


