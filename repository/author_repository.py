from sqlalchemy.orm import Session

from model.models import Author


def list_all(db: Session):
    return db.query(Author).all()


def find_by_id(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()
