from sqlalchemy.orm import Session

from model.models import Book
from model.schemas import BookCreate, BookUpdate


def list_all(db: Session):
    return db.query(Book).all()


def find_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def save(db: Session, book_create: BookCreate):
    # TODO 8: Create a new Book instance and save it to the database
    pass


def update(db: Session, book_update: BookUpdate, book_id: int):
    # TODO 9: Find the book, and if it exists, update only the fields provided in book_update
    pass


def delete_by_id(db: Session, book_id: int):
    # TODO 10: Find the book and remove it from the database
    pass
