from sqlalchemy.orm import Session

from database.database import SessionLocal, engine
from model.models import Base, Author, Book, User, Cart


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def seed_data(db: Session):
    author1 = Author(name="George Orwell", biography="English novelist and critic.")
    author2 = Author(name="Aldous Huxley", biography="English writer and philosopher.")
    author3 = Author(name="Ray Bradbury", biography="American author and screenwriter.")
    db.add_all([author1, author2, author3])
    db.flush()

    books = [
        Book(title="1984", price=9.99, quantity=10, category="Dystopian", author_id=author1.id),
        Book(title="Animal Farm", price=6.99, quantity=15, category="Satire", author_id=author1.id),
        Book(title="Brave New World", price=12.50, quantity=20, category="Science Fiction", author_id=author2.id),
        Book(title="Island", price=10.00, quantity=5, category="Philosophical", author_id=author2.id),
        Book(title="Fahrenheit 451", price=11.00, quantity=25, category="Dystopian", author_id=author3.id),
        Book(title="The Martian Chronicles", price=13.99, quantity=7, category="Sci-Fi", author_id=author3.id),
        Book(title="Dandelion Wine", price=8.75, quantity=18, category="Fiction", author_id=author3.id),
        Book(title="Something Wicked", price=9.50, quantity=12, category="Fantasy", author_id=author3.id),
    ]
    db.add_all(books)

    user = User(username="test", email="test@test.com", password="test123")
    db.add(user)
    db.flush()

    cart = Cart(user_id=user.id)
    db.add(cart)

    db.commit()


def seed():
    reset_database()
    db = SessionLocal()

    try:
        seed_data(db)
        print("Seeded 3 authors, 8 books, 1 user with cart.")

    except Exception as e:
        db.rollback()
        print(f"Seeding failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
