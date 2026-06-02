from sqlalchemy.orm import Session

from model.models import Book
from model.schemas import BookCreate, BookUpdate


def list_all(db: Session):
    return db.query(Book).all()


def find_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def save(db: Session, book_create: BookCreate):
    # TODO 8: Create a new Book instance and save it to the database
    new_book = Book(**book_create.model_dump())

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def update(db: Session, book_update: BookUpdate, book_id: int):
    # TODO 9: Find the book, and if it exists, update only the fields provided in book_update
    db_book = find_by_id(db, book_id)

    if not db_book:
        return None

    for key, value in book_update.model_dump(exclude_unset=True).items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_by_id(db: Session, book_id: int):
    # TODO 10: Find the book and remove it from the database
    db_book = find_by_id(db, book_id)

    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book
