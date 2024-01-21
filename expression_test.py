import pytest

from exceptions import SyntaxException
from solve_expression import ExpressionSolver


@pytest.mark.parametrize(
    "expression, expectation",
    [
        ("2*^3",
         "In the left side of * operation - you need to have two expressions "
         "and no operation other than right orientation - Right syntax - x * y"),
        ("(2+6))",
         "You can't have a closing parentheses without opening first"),
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





        ("1+1", 2),
        ("2^3", 8.0),
        ("3--2", 5),
        ("-10+-8", -18),
        ("-9/-3", 3.0),
        ("(12+10)@44", 33.0),
        ("2*6", 12),
        ("-3*-7", 21),
        ("(2+1)!", 6),
        ("3&7", 3),
        ("-5$10", -10),
        ("~5$10", 10),
        ("20 % 3", 2),
        ("(2+9)#", 2),
        ("9/0",
         "division by zero"),
        ("0^-5",
         "Can't have a 0 in power of a number smaller than 1"),

        ("--(12+69*0.5)/(-2^3+65)+(3!)#@(~-3)", 5.3157894737),
        ("33+50/5+98--5+6*(12 % 5@4+9#-2!&1)", 212.0),
        ("~7+9&-8+(5!-100)  / (24 $ 6 % 5)-17+12@6", -18.0),
        ("(5!+220)/2*(200 & 50 - 6 $ (99 % 50)) + (~-220)# + 4^2 + 55#", 200.0),
        ("(45+6/2)# + 90-~10 + (12 & 45)/((120 ^ 0) $ 12) + 22.5*2", 158.0),
        ("5!#! + 96 $ 12 + (20 * 4 + 80 & 20) + 3.4$3 + 16^(0.25@0.75)", 209.4),
        ("-12^2 - (((49^0.5)@1) + 40) + 5 * (24-8*6+12) + (5!/100)", 41.2),
        ("6 & 2^3$4 + 5- 9 /3 + 7^2 -- 3.7 - 8 / 4 + 6.4# - 2.7#", 69.7),
        ("((12 @ 8 + 9)##! +12+ 8-5! + 90*2)# + 12 & (0 @ 20) + 9 $ (7*5-9+22)", 67.0),
        ("100 - (100 @ 50 - 25 $ (2^5@3) + 2! * 6) - (~--10 - 50 % 49 - 5 * 9 - (20 + 2 ^ 2)#)", 100.0),
        ("7 & 2 @ 4 + 1 - 4^3 /2 +9 - (2 * 6) / 4 + (6.8 - 2.4)", -17.6),
        ("10$4/(2 * 2!) -3 ! + 12 + (4^2)# + 8.6 - 3.5 / 7 + 6.2", 29.8),
        ("(2! + (7! - 7^3)# + 12 + 6 - 8 * 3 + (7 ^ 2) % 23 & 5)", 26.0),
        ("125 - 5^2@0 + 12 $ (12+56) - (5! - 8*7 - 100 + 55* 2 + 99.6#)", 90.0),
        ("12+98 + (-12*-2 + 8 ^ 0 + 5 & -5 ) % 2 + (5!)# @ (6!)#", 116.0),
        ("4/2 % 6@3 -1 - 2.4 -39 + 7 * (6.8 - 1.2 * 5) / 0.5 + (2.6 - 9.1)", -36.6),
        ("((~-45 + 8)# / 2)! + 12 + 9 * (12 + 7*20 - 20*(14@0) - 9 % 2 $ 9) & 95", 144.0),
        ("(~-4) ^ 2$3 + (3@(10 & 1)/2 -8^2 + 6) - (4.2 / 2.1 * (7 + 4))", -8.399999999999999),
        ("7 - (12# + 2^2)@13 + 6^2 +15 + 2.3 - 4.6# $ 9.2 + 1.5 / 3", 40.8),
        ("(2+9 * (2^((15%5) & --(8@2))) - 2.5 + 5 / 2 )&(45 * 2!)$(100 - 65 + 12# + (62*2) * 0.5)", 100.0)
    ])
def test_expression(expression, expectation):
    try:
        s = ExpressionSolver(expression)
        result = s.solve()
        assert result == expectation
    except (SyntaxException, ZeroDivisionError, ArithmeticError) as exc:
        assert str(exc) == expectation
