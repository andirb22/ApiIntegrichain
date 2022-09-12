from distutils.command.config import config
from models import configDB
from models.configDB import db,app,ma
from flask import  request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.models_entity import Books
from flask import Blueprint
from utils.request_utils import get_request_json,serialize_response
from services import book_service
from flask import current_app



BOOKS_CONTROLLER = Blueprint(
    'Books_Controller', __name__)
    
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author','read')
        
book_schema = BookSchema()
books_schema = BookSchema(many=True)

@app.route('/books', methods=['Post'])
def save_book():
    book_ = get_request_json()
    book_id=book_service.save_book(book_)
    return 'id Added: ' + str(book_id)

    
@app.route('/books', methods=['GET'])
def get_books():
    all_books=book_service.gett_all_books()
    return jsonify(all_books)


@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book_=book_service.get_book_by_id(id)
    book_ser= book_schema.jsonify(book_)
    return book_ser

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = get_request_json()
    book_response=book_service.update_book(id,book)
    return book_schema.jsonify(book_response)
    

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book_service.delete_book(id)
    return jsonify({'message': 'Record Deleted',"Book ID":id})



@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'})
