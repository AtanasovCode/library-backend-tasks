from sqlalchemy.orm import Session

from model.models import Cart, CartItem, Book
from model.schemas import CartItemCreate


def get_cart_by_user(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).first()


def create_cart(db: Session, user_id: int):
    new_cart = Cart(user_id=user_id)
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart


def add_item_to_cart(db: Session, cart_id: int, item_data: CartItemCreate):
    # TODO 11: Create a new CartItem and add it to the given cart\
    pass


def remove_item_from_cart(db: Session, cart_id: int, item_id: int):
    # TODO 12: Find the CartItem by cart_id and item_id, then delete it if it exists
    pass


def clear_cart(db: Session, cart_id: int):
    # TODO 13: Remove all items from the cart with the given ID
    pass


def buy_items(db: Session, cart_id: int):
    # TODO 14: Reduce quantity of each book in the cart if enough stock is available,
    # raise ValueError on insufficient stock, then clear the cart
    pass


def get_cart_items(db: Session, cart_id: int):
    return db.query(CartItem).filter(CartItem.cart_id == cart_id).all()
