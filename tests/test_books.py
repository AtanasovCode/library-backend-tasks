from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_list_all_books_5p():
    response = client.get("/api/books")
    assert response.status_code == 200

    books = response.json()
    assert isinstance(books, list)
    assert len(books) == 8


def test_find_book_by_id_5p():
    response = client.get("/api/books/1")
    assert response.status_code == 200

    book = response.json()
    assert book["id"] == 1
    assert "title" in book
    assert "author" in book


def test_create_book_15p():
    book_data = {
        "title": "Test Book",
        "price": 19.99,
        "quantity": 10,
        "category": "Test",
        "author_id": 1
    }

    create_response = client.post("/api/books", json=book_data)
    assert create_response.status_code == 200
    created = create_response.json()
    assert created["id"] == 9
    assert created["title"] == "Test Book"

    list_response = client.get("/api/books")
    assert list_response.status_code == 200
    books = list_response.json()
    assert len(books) == 9

    find_response = client.get("/api/books/9")
    assert find_response.status_code == 200
    book = find_response.json()
    assert book["title"] == book_data["title"]
    assert book["price"] == book_data["price"]
    assert book["quantity"] == book_data["quantity"]
    assert book["category"] == book_data["category"]
    assert book["author"]["id"] == book_data["author_id"]


def test_update_book_15p():
    update_data = {
        "title": "Edited Title",
        "price": 1.99,
        "quantity": 20
    }

    response = client.put("/api/books/1", json=update_data)
    assert response.status_code == 200
    updated_book = response.json()

    assert updated_book["id"] == 1
    assert updated_book["title"] == update_data["title"]
    assert updated_book["price"] == update_data["price"]
    assert updated_book["quantity"] == update_data["quantity"]


def test_delete_book_10p():
    list_response = client.get("/api/books")
    assert list_response.status_code == 200
    books = list_response.json()

    client.delete("/api/books/8")

    get_response = client.get("/api/books/8")
    assert get_response.status_code == 404

    list_response = client.get("/api/books")
    assert list_response.status_code == 200
    books1 = list_response.json()
    assert len(books) - 1 == len(books1)


def test_add_item_to_cart_15p():
    payload = {
        "book_id": 1
    }

    response = client.post("/api/cart/1/add-item", json=payload)
    assert response.status_code == 200
    added_item = response.json()
    assert added_item["book"]["id"] == 1

    cart_response = client.get("/api/cart/user/1")
    assert cart_response.status_code == 200

    cart = cart_response.json()
    items = cart["cart_items"]
    assert any(item["book"]["id"] == 1 for item in items)


def test_remove_item_from_cart_10p():
    payload = {
        "book_id": 1
    }
    add_response = client.post("/api/cart/1/add-item", json=payload)
    assert add_response.status_code == 200

    cart_response = client.get("/api/cart/user/1")
    assert cart_response.status_code == 200
    cart = cart_response.json()
    items = cart["cart_items"]
    assert len(items) > 0

    item_id = items[0]["id"]

    delete_response = client.delete(f"/api/cart/1/items/{item_id}")
    assert delete_response.status_code == 200
    assert f"Item {item_id} removed" in delete_response.json()["message"]

    final_cart = client.get("/api/cart/user/1").json()
    assert all(item["id"] != item_id for item in final_cart["cart_items"])


def test_clear_cart_10p():
    payload = {
        "book_id": 1
    }
    client.post("/api/cart/1/add-item", json=payload)

    cart_before = client.get("/api/cart/user/1").json()
    assert len(cart_before["cart_items"]) > 0

    clear_response = client.delete("/api/cart/1/clear")
    assert clear_response.status_code == 200
    assert "cleared successfully" in clear_response.json()["message"]

    cart_after = client.get("/api/cart/user/1").json()
    assert cart_after["cart_items"] == []


def test_buy_items_reduces_product_quantity_15p():
    book_before = client.get("/api/books/1").json()
    initial_quantity = book_before["quantity"]

    payload = {
        "book_id": 1
    }
    add_response = client.post("/api/cart/1/add-item", json=payload)
    assert add_response.status_code == 200

    buy_response = client.post("/api/cart/1/buy_items")
    assert buy_response.status_code == 200
    assert "bought successfully" in buy_response.json()["message"]

    cart = client.get("/api/cart/user/1").json()
    assert cart["cart_items"] == []

    book_after = client.get("/api/books/1").json()
    assert book_after["quantity"] == initial_quantity - 1
