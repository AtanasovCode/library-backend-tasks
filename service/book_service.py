from sqlalchemy.orm import Session

from model.schemas import BookCreate, BookUpdate
from repository import book_repository


# CRUD

def list_all(db: Session):
    return book_repository.list_all(db)


# R - retrieve
def find_by_id(db: Session, book_id: int):
    return book_repository.find_by_id(db, book_id)


# C - create
def save(db: Session, book_create: BookCreate):
    return book_repository.save(db, book_create)


# U - update
def update(db: Session, book_update: BookUpdate, book_id: int):
    return book_repository.update(db, book_update, book_id)


# D - delete
def delete(db: Session, book_id: int):
    book_repository.delete_by_id(db, book_id)
