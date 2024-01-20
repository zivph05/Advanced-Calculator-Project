import pytest

from exceptions import SyntaxException
from solve_expression import ExpressionSolver


@pytest.mark.parametrize(
    "expression, expectation",
    [
        ("0^-5",
         "Can't have a 0 in power of a number smaller than 1"),
        ("2*^3",
         "In the left side of * operation - you need to have two expressions "
         "and no operation other than right orientation - Right syntax - x * y"),
        ("9/0",
         "division by zero"),
        ("1+1", "2")
    ])
def test_expression(expression, expectation):
    try:
        s = ExpressionSolver(expression)
        result = s.solve()
        assert str(result) == expectation
    except SyntaxException as exc:
        assert str(exc) == expectation
    except (ZeroDivisionError, ArithmeticError) as exc:
        assert str(exc) == expectation

