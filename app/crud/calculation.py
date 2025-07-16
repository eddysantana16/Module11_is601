from sqlalchemy.orm import Session
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate
from app.services.calculation_factory import CalculationFactory


def create_calculation(db: Session, calc_in: CalculationCreate, user_id: int = None) -> Calculation:
    operation = CalculationFactory.get_operation(calc_in.type)
    result = operation.execute(calc_in.a, calc_in.b)

    new_calc = Calculation(
        a=calc_in.a,
        b=calc_in.b,
        type=calc_in.type,
        result=result,
        user_id=user_id  # Optional field
    )

    db.add(new_calc)
    db.commit()
    db.refresh(new_calc)
    return new_calc


def get_calculation_by_id(db: Session, calc_id: int) -> Calculation:
    return db.query(Calculation).filter(Calculation.id == calc_id).first()
