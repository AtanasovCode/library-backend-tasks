import pytest

from database.database import get_db
from database.seed import reset_database, seed_data


@pytest.fixture(scope="session", autouse=True)
def prepare_test_db():
    reset_database()
    db = next(get_db())
    seed_data(db)
    db.close()
