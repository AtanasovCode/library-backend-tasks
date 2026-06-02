from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database.database import get_db
from model.schemas import AuthorSchema
from service import author_service

router = APIRouter(prefix="/api/authors", tags=["Author"])


@router.get("", response_model=list[AuthorSchema])
async def list_authors(db: Session = Depends(get_db)):
    return author_service.list_all(db)


@router.get("/{author_id}", response_model=AuthorSchema)
async def find_author(author_id: int, db: Session = Depends(get_db)):
    author = author_service.find_by_id(db, author_id)
    if author is not None:
        return author
    return JSONResponse(status_code=404, content={"message": f"Author with id {author_id} not found"})
