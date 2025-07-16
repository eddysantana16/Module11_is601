from pydantic import BaseModel, Field, field_validator
from enum import Enum
from typing import Optional
from pydantic import ConfigDict


class CalculationType(str, Enum):
    ADD = "Add"
    SUB = "Sub"
    MULTIPLY = "Multiply"
    DIVIDE = "Divide"


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: CalculationType

    @field_validator("b")
    @classmethod
    def check_divide_by_zero(cls, b_value, values):
        if values.data.get("type") == CalculationType.DIVIDE and b_value == 0:
            raise ValueError("Cannot divide by zero.")
        return b_value

class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: CalculationType
    result: Optional[float] = None
    user_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

