from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database.database import get_db
from model.schemas import BookSchema, BookCreate, BookUpdate
from service import book_service

router = APIRouter(prefix="/api/books", tags=["Book"])


@router.get("", response_model=list[BookSchema])
async def list_books(db: Session = Depends(get_db)):
    return book_service.list_all(db)


@router.get("/{book_id}", response_model=BookSchema)
async def find_book(book_id: int, db: Session = Depends(get_db)):
    book = book_service.find_by_id(db, book_id)
    if book is not None:
        return book
    return JSONResponse(status_code=404, content={"message": f"Book with id {book_id} not found"})


# TODO 15: Annotate the method with the correct mapping (path = "")
@router.post("", response_model=BookSchema)
async def create_book(book_create: BookCreate, db: Session = Depends(get_db)):
    return book_service.save(db, book_create)


# TODO 16: Annotate the method with the correct mapping (path = "/{book_id}")
@router.put("/{book_id}", response_model=BookSchema)
async def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    book = book_service.find_by_id(db, book_id)
    if book is not None:
        return book_service.update(db, book_update, book_id)
    return JSONResponse(status_code=404, content={"message": f"Book with id {book_id} not found"})


# TODO 17: Annotate the method with the correct mapping (path = "/{book_id}")
@router.delete("/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = book_service.find_by_id(db, book_id)
    if book is not None:
        book_service.delete(db, book.id)
        return JSONResponse(status_code=200, content={"message": f"Book with id {book_id} deleted successfully"})
    return JSONResponse(status_code=404, content={"message": f"Book with id {book_id} not found"})
