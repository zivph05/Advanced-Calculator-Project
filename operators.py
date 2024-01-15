from math import pow

from exceptions import ExpressionException, SyntaxException

operators = {'+': 1, '-': 1, '*': 2, '_': 2, '/': 2, '^': 3, 'u': 7, '%': 4, '@': 5, '$': 5, '&': 5, '~': 6, '!': 6,
             '#': 5}
rep = ['_', 'u']


def op_type(op):
    if op == '~' or op == 'u' or op == '_':
        return 'r'
    elif op == '!' or op == '#':
        return 'l'
    return 'm'


def count(op):
    res = 0
    str_op = str(op)
    a = str_op.split('.')
    for index in range(0, len(a)):
        for index_1 in range(0, len(a[index])):
            ch = a[index][index_1]
            res += int(ch)
    return res


def factorial(op):
    """
    Calculates the factorial of a number (op!)
    :param op: the number in calculation
    :return: the factorial of op (op!)
    """
    res = 1.0

    if op == float('inf'):
        return float('inf')

    op_int = int(op)
    for i in range(2, op + 1):
        if res == float('inf'):
            return float('inf')
        res *= i
    return res


def mean(op1, op2):
    """
    Calculates the mean of op1 of op2 (op1 @ op2)
    :param op1: the first number in the mean
    :param op2: the second number in the mean
    :return: mean of op1 and op2 (op1 @ op2)
    """
    return (op1 + op2) / 2


def calculate(op1, op2, operation):
    """
    Calculates the ex. that is given
    :param op1: the first operand
    :param op2: the second operand
    :param operation: the operation
    :return: result of the ex. (op1 ___ op2)
    raises: if in ! operation has a float value or a negative number
    """
    res = 0

    # Check if the expression isn't valid

    # Check the operation and operate as such
    match operation:
        case '+':
            res = op1 + op2
        case '-':
            res = op1 - op2
        case '*':
            res = op1 * op2
        case '/':
            if op2 == 0:
                message = "Can't have second operand be zero in division:", op1, "/", op2
                raise ExpressionException(message)
            res = op1 / op2
        case '^':
            if op1 < 0 and (-1 < op2 < 1) and op2 != 0:
                raise ExpressionException("Can't have a negative number be in root of (when the second op is between "
                                          "1 and -1 and not zero)")
            if op1 == 0 and op2 < 1:
                raise ExpressionException("Can't have a 0 in power of a number smaller than 1")
            try:
                res = pow(op1, op2)
            except OverflowError:
                res = float('inf')
        case '%':
            res = op1 % op2
        case '~':
            res = -op2
        case '@':
            res = mean(op1, op2)
        case '$':
            res = max(op1, op2)
        case '&':
            res = min(op1, op2)
        case '!':
            if (op1 % 1) != 0 and op1 != float('inf'):
                raise ExpressionException("Factorial can't have a float as an operand")
            elif op1 < 0:
                raise ExpressionException("Can't calculate a factorial on a negative number")
            res = factorial(op1)
        case '#':
            if op1 < 0:
                raise ExpressionException("Can't calculate a counting expression on a negative number")
            res = count(op1)
        case 'u':
            res = -op2
        case '_':
            res = -op2
    return res


def priority(operation):
    """
    Gives the "power of" the operation given
    :param operation: the operation that is being evaluated
    :return: the power of the operation given
    """
    # Check the operation and return the "power of" the operation
    return operators.get(operation)


def check_validity(op1, op2, operation):
    """
    Checks if the operation at hand is valid
    :param op1: part of operation - first operand
    :param op2: part of operation - second operand
    :param operation: part of operation - operation
    :return: if operation is valid
    :raises: if operation is not in the right syntax...
    """

    if (op1 is None or op2 is None) and op_type(operation) == 'm':
        message = ("Operation is not acceptable, you need the two operands to be other than none...\nRight Syntax: x %s"
                   % operation, "y")
        raise SyntaxException(message)

    if (op1 is not None or op2 is None) and op_type(operation) == 'r':
        message = ("Operation is not acceptable, in ", operation, "operation, you need the first operand to be none "
                                                                  "and the second one needs to be other than none... "
                                                                  "\nRight syntax:", operation, "x")

        if operation == 'u' or operation == '_':
            message = ("Operation is not acceptable, in unary - operation, you need the first operand to be none "
                       "and the second one needs to be other than none... \nRight syntax: -x")
        raise SyntaxException(message)

    if (op1 is None or op2 is not None) and op_type(operation) == 'l':
        message = ("Operation is not acceptable, in ", operation, "operation, you need the second operand to be "
                                                                  "none... \nRight syntax: x", operation)
        raise SyntaxException(message)
    return True


def is_operator(ch):
    """
    Checks if char given is in operators list
    :param ch: the char in check
    :return: True if char given is in operators list, else False.
    """
    return ch in operators
