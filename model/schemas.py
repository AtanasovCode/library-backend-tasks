from typing import Optional, List
from pydantic import BaseModel


# TODO 7: These should be schemas used for data validation and serialization

class AuthorSchema(BaseModel):
    id: int
    name: str
    biography: Optional[str] = None


class BookSchema(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    category: str
    author: AuthorSchema


class BookCreate(BaseModel):
    title: str
    price: float
    quantity: int
    category: str
    author_id: int


class BookUpdate(BaseModel):
    title: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category: Optional[str] = None
    author_id: Optional[int] = None


class UserSchema(BaseModel):
    id: int
    username: str
    email: str

class CartItemSchema(BaseModel):
    id: int
    book: BookSchema


class CartItemCreate(BaseModel):
    book_id: int


class CartSchema(BaseModel):
    id: int
    user: UserSchema
    cart_items: List[CartItemSchema] = []


class CartCreate():
    user_id: int