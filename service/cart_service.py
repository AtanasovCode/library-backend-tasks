from sqlalchemy.orm import Session

from model.schemas import CartItemCreate
from repository import cart_repository


def get_cart_by_user(db: Session, user_id: int):
    return cart_repository.get_cart_by_user(db, user_id)


def create_cart(db: Session, user_id: int):
    return cart_repository.create_cart(db, user_id)


def add_item_to_cart(db: Session, cart_id: int, item_data: CartItemCreate):
    return cart_repository.add_item_to_cart(db, cart_id, item_data)


def remove_item_from_cart(db: Session, cart_id: int, item_id: int):
    return cart_repository.remove_item_from_cart(db, cart_id, item_id)


def clear_cart(db: Session, cart_id: int):
    return cart_repository.clear_cart(db, cart_id)


def buy_items(db: Session, cart_id: int):
    return cart_repository.buy_items(db, cart_id)


def get_cart_items(db: Session, cart_id: int):
    return cart_repository.get_cart_items(db, cart_id)
