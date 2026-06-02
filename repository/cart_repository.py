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
    # TODO 11: Create a new CartItem and add it to the given cart
    new_item = CartItem(
        cart_id = cart_id,
        book_id = item_data.book_id
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def remove_item_from_cart(db: Session, cart_id: int, item_id: int):
    # TODO 12: Find the CartItem by cart_id and item_id, then delete it if it exists
    cart_item = db.query(CartItem).filter(
        CartItem.cart_id == cart_id,
        CartItem.book_id == item_id
    ).first()

    if not cart_item:
        return None

    db.delete(cart_item)
    db.commit()
    return cart_item


def clear_cart(db: Session, cart_id: int):
    # TODO 13: Remove all items from the cart with the given ID
    db.query(CartItem).filter(
        CartItem.cart_id == cart_id
    ).delete()
    db.commit()


def buy_items(db: Session, cart_id: int):
    # TODO 14: Reduce quantity of each book in the cart if enough stock is available,
    # raise ValueError on insufficient stock, then clear the cart

    cart_items = db.query(CartItem).filter(CartItem.cart_id == cart_id).all()

    for item in cart_items:
        book = db.query(Book).filter(Book.id == item.book_id).first()

        if not book or book.quantity < 1:
            raise ValueError(f"Insufficient stock for item {item.book_id}")

        book.quantity -= 1
        db.delete(item)
    db.commit()


def get_cart_items(db: Session, cart_id: int):
    return db.query(CartItem).filter(CartItem.cart_id == cart_id).all()
