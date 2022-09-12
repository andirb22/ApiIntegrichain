from typing import List
from models.models_entity import Books
from models.configDB import db,ma
from flask import  request, jsonify

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author','read')
        
book_schema = BookSchema()
books_schema = BookSchema(many=True)

        
def save_book(request: dict) -> int:
    title=request["title"]
    author=request["author"]
    read=request["read"]
    new_book=Books(title,author,read)
    db.session.add(new_book)
    db.session.commit()
    return new_book.id
    #return book_schema.jsonify(new_book)
    
def gett_all_books() -> List[dict]:
    all_books = Books.query.all()
    result = books_schema.dump(all_books)
    return result

def update_book(book_id: int, request: dict) -> None:
    book = Books.query.get(book_id)
    title=request["title"]
    author=request["author"]
    read=request["read"]
    book.title = title
    book.author = author
    book.read=read
    db.session.commit()
    return book


def delete_book(book_id: int) -> None:
    book = Books.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    



def get_book_by_id(book_id: int) -> dict:
    book_1=Books.query.get(book_id)
    return book_1
