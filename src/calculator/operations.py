from dataclasses import dataclass

class CalculatorError(Exception):
    """Base error for calculator problems."""

class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

@dataclass
class Calculator:
    """Stateless arithmetic operations using methods (OOP)."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def sub(self, a: float, b: float) -> float:
        return a - b

    def mul(self, a: float, b: float) -> float:
        return a * b

    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Division by zero is not allowed.")
        return a / b
