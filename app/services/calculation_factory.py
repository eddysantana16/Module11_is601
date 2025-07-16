from enum import Enum

class CalculationType(str, Enum):
    ADD = "Add"
    SUB = "Sub"
    MULTIPLY = "Multiply"
    DIVIDE = "Divide"

# Individual calculation classes
class Add:
    @staticmethod
    def execute(a: float, b: float) -> float:
        return a + b

class Sub:
    @staticmethod
    def execute(a: float, b: float) -> float:
        return a - b

class Multiply:
    @staticmethod
    def execute(a: float, b: float) -> float:
        return a * b

class Divide:
    @staticmethod
    def execute(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Factory function
class CalculationFactory:
    @staticmethod
    def get_operation(calc_type: CalculationType):
        if calc_type == CalculationType.ADD:
            return Add
        elif calc_type == CalculationType.SUB:
            return Sub
        elif calc_type == CalculationType.MULTIPLY:
            return Multiply
        elif calc_type == CalculationType.DIVIDE:
            return Divide
        else:
            raise ValueError(f"Unsupported calculation type: {calc_type}")
