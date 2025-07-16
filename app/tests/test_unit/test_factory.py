import pytest
from app.services.calculation_factory import CalculationFactory, CalculationType


def test_add_operation():
    op = CalculationFactory.get_operation(CalculationType.ADD)
    assert op.execute(2, 3) == 5


def test_sub_operation():
    op = CalculationFactory.get_operation(CalculationType.SUB)
    assert op.execute(5, 2) == 3


def test_multiply_operation():
    op = CalculationFactory.get_operation(CalculationType.MULTIPLY)
    assert op.execute(4, 3) == 12


def test_divide_operation():
    op = CalculationFactory.get_operation(CalculationType.DIVIDE)
    assert op.execute(10, 2) == 5


def test_divide_by_zero():
    op = CalculationFactory.get_operation(CalculationType.DIVIDE)
    with pytest.raises(ValueError):
        op.execute(10, 0)


def test_invalid_type():
    with pytest.raises(ValueError):
        CalculationFactory.get_operation("Square")
