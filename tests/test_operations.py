import math
import pytest
from calculator.operations import Calculator, DivisionByZeroError

calc = Calculator()

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_add(a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (0, 3, -3),
        (-2.5, -0.5, -2.0),
    ],
)
def test_sub(a, b, expected):
    assert calc.sub(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 4, 12),
        (-2, 3, -6),
        (1.5, 2, 3.0),
    ],
)
def test_mul(a, b, expected):
    assert calc.mul(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (3, 2, 1.5),
        (-9, -3, 3),
    ],
)
def test_div(a, b, expected):
    assert math.isclose(calc.div(a, b), expected)

def test_div_by_zero():
    with pytest.raises(DivisionByZeroError):
        calc.div(1, 0)
