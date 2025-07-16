import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.session import Base
from app.schemas.calculation import CalculationCreate, CalculationType
from app.crud.calculation import create_calculation, get_calculation_by_id

# Match your exposed Docker port (5432 or 5433)
DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/calculator_db"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_and_get_calculation(test_db):
    calc_data = CalculationCreate(a=10, b=2, type=CalculationType.DIVIDE)
    created = create_calculation(test_db, calc_data)
    fetched = get_calculation_by_id(test_db, created.id)

    assert fetched is not None
    assert fetched.result == 5.0
    assert fetched.type == "Divide"
