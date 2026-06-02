from typing import Optional, List


# TODO 7: These should be schemas used for data validation and serialization

class AuthorSchema():
    id: int
    name: str
    biography: Optional[str] = None


class BookSchema():
    id: int
    title: str
    price: float
    quantity: int
    category: str
    author: AuthorSchema


class BookCreate():
    title: str
    price: float
    quantity: int
    category: str
    author_id: int


class BookUpdate():
    title: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category: Optional[str] = None
    author_id: Optional[int] = None


class UserSchema():
    id: int
    username: str
    email: str

class CartItemSchema():
    id: int
    book: BookSchema


class CartItemCreate():
    book_id: int


class CartSchema():
    id: int
    user: UserSchema
    cart_items: List[CartItemSchema] = []


class CartCreate():
    user_id: int