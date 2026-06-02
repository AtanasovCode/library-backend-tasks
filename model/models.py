from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# TODO 1: Make the classes be database tables
class Author():
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    biography = Column(String)

    # TODO 2: Define a one-to-many relationship with books (an author can have multiple books)


class Book():
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    category = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))

    # TODO 3: Define the reverse side of the author–book relationship

class User():
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    # TODO 4: Link the user to their cart (one-to-one)

class Cart():
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="cart")

    # TODO 5: Define the one-to-many relationship to cart items


class CartItem():
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    # TODO 6: Set up relationships back to Cart and Book
