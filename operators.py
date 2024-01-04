from exceptions import ExpressionException


def factorial(op: int) -> int:
    """
    Calculates the factorial of a number (op!)
    :param op: the number in calculation
    :return: the factorial of op (op!)
    """
    res = 1
    for i in range(2, op):
        res *= i
    return res


# put in int or float?
def mean(op1, op2):
    """
    Calculates the mean of op1 of op2 (op1 @ op2)
    :param op1: the first number in the mean
    :param op2: the second number in the mean
    :return: mean of op1 and op2 (op1 @ op2)
    """
    return (op1 + op2) / 2


def calculate(op1, op2, operation: str):
    """
    Calculates the ex. that is given
    :param op1: the first operand
    :param op2: the second operand
    :param operation: the operation
    :return: result of the ex. (op1 ___ op2)
    """
    res = 0

    # Check the operation and operate as such
    match operation:
        case '+':
            res = op1 + op2
        case '-':
            res = op1 - op2
        case '*':
            res = op1 * op2
        case '/':
            res = op1 / op2
        case '^':
            res = op1 ** op2
        case '%':
            res = op1 % op2
        case '~':
            res = -op1
        case '@':
            res = mean(op1, op2)
        case '$':
            res = max(op1, op2)
        case '&':
            res = min(op1, op2)
        case '!':
            if operation != '!':
                if isinstance(op1, float):
                    raise ExpressionException("Factorial can't have a float as an operand")
                elif op1 < 0:
                    raise ExpressionException("Can't calculate a factorial on a negative number")
            res = factorial(op1)
    return res


def otzma(operation: str) -> int:
    """
    Gives the "power of" the operation given
    :param operation: the operation that is being evaluated
    :return: the power of the operation given
    """
    # Check the operation and return the "power of" the operation
    match operation:
        case '+':
            return 1
        case '-':
            return 1
        case '*':
            return 2
        case '/':
            return 2
        case '^':
            return 3
        case '%':
            return 4
        case '~':
            return 6
        case '@':
            return 5
        case '$':
            return 5
        case '&':
            return 5
        case '!':
            return 6
