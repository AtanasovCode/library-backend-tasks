from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database.database import get_db
from model.schemas import CartItemCreate, CartSchema, CartItemSchema
from service import cart_service

router = APIRouter(prefix="/api/cart", tags=["Cart"])


@router.get("/user/{user_id}", response_model=CartSchema)
async def get_cart(user_id: int, db: Session = Depends(get_db)):
    cart = cart_service.get_cart_by_user(db, user_id)
    if cart:
        return cart
    return JSONResponse(status_code=404, content={"message": f"Cart for user {user_id} not found"})


@router.post("/user/{user_id}", response_model=CartSchema)
async def create_cart(user_id: int, db: Session = Depends(get_db)):
    return cart_service.create_cart(db, user_id)


# TODO 18: Annotate the method with the correct mapping on path "/{cart_id}/add-item"
@router.post("/{cart_id}/add-item", response_model=CartItemSchema)
async def add_item(cart_id: int, item_data: CartItemCreate, db: Session = Depends(get_db)):
    return cart_service.add_item_to_cart(db, cart_id, item_data)


# TODO 19: Annotate the method with the correct mapping on path "/{cart_id}/items/{item_id}"
@router.delete("/{cart_id}/items/{item_id}")
async def remove_item(cart_id: int, item_id: int, db: Session = Depends(get_db)):
    item = cart_service.remove_item_from_cart(db, cart_id, item_id)
    if item:
        return JSONResponse(status_code=200, content={"message": f"Item {item_id} removed from cart {cart_id}"})
    return JSONResponse(status_code=404, content={"message": f"Item {item_id} not found in cart {cart_id}"})


# TODO 20: Annotate the method with the correct mapping on path "/{cart_id}/clear"
@router.delete("/{cart_id}/clear")
async def clear_cart(cart_id: int, db: Session = Depends(get_db)):
    cart_service.clear_cart(db, cart_id)
    return JSONResponse(status_code=200, content={"message": f"Cart {cart_id} cleared successfully"})


# TODO 21: Annotate the method with the correct mapping on path "/{cart_id}/buy_items"
@router.post("/{cart_id}/buy_items", response_model=CartSchema)
async def buy_items(cart_id: int, db: Session = Depends(get_db)):
    try:
        cart_service.buy_items(db, cart_id)
        return JSONResponse(status_code=200, content={"message": f"Items from Cart: {cart_id} bought successfully"})
    except ValueError as e:
        return JSONResponse(status_code=400, content={"message": str(e)})


@router.get("/{cart_id}/items", response_model=List[CartItemSchema])
async def get_cart_items(cart_id: int, db: Session = Depends(get_db)):
    cart_items = cart_service.get_cart_items(db, cart_id)
    return cart_items
