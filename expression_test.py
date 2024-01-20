import pytest

from exceptions import SyntaxException
from solve_expression import ExpressionSolver


@pytest.mark.parametrize(
    "expression, expectation",
    [
        ("2*^3",
         "In the left side of * operation - you need to have two expressions "
         "and no operation other than right orientation - Right syntax - x * y"),
        ("5+&8",
         "In the left side of + operation - you need to have two expressions "
         "and no operation other than right orientation - Right syntax - x + y"),
        ("!6+6",
         "In ! expression - the right syntax is x!"),
        ("5~-6",
         "In the right side of ~ operation - you need to have an expression to the right, "
         "and no operation that has an orientation other than left - Right syntax - ~ x"),
        ("~~9",
         "In ~ action, you need to have only an expression or an unary minus"),

        ("", "Nothing Entered..."),
        ("asdfdghhfds", "Unidentified character"),
        ("  \t", "Nothing Entered..."),





        ("1+1", "2"),
        ("2^3", "8.0"),
        ("3--2", "5"),
        ("-10+-8", "-18"),
        ("-9/-3", "3.0"),
        ("(12+10)@44", "33.0"),
        ("2*6", "12"),
        ("-3*-7", "21"),
        ("(2+1)!", "6"),
        ("3&7", "3"),
        ("-5$10", "-10"),
        ("~5$10", "10"),
        ("20 % 3", "2"),
        ("(2+9)#", "2"),
        ("9/0",
         "division by zero"),
        ("0^-5",
         "Can't have a 0 in power of a number smaller than 1"),

        ("--(12+69*0.5)/(-2^3+65)+(3!)#@(~-3)", "5.3157894737"),
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

