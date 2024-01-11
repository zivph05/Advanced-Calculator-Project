from exceptions import ExpressionException, SyntaxException

operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '@': 5, '$': 5, '&': 5, '~': 6, '!': 6, '#': 5}


def op_type(op):
    if op == '~':
        return 'r'
    elif op == '!' or op == '#':
        return 'l'
    return 'm'


def count(op):
    res = 0
    while op > 10:
        res += int(op % 10)
        op /= 10
    return res + int(op)


def factorial(op):
    """
    Calculates the factorial of a number (op!)
    :param op: the number in calculation
    :return: the factorial of op (op!)
    """
    res = 1
    for i in range(2, op + 1):
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
    #
    # try:
    #    check_validity(op1, op2, operation)
    # except ExpressionException:
    #    pass

    # Check the operation and operate as such
    match operation:
        case '+':
            res = op1 + op2
        case '-':
            if op1 == 0:
                res = -op2
            else:
                res = op1 - op2
        case '*':
            res = op1 * op2
        case '/':
            if op2 == 0:
                raise ExpressionException("Can't have second operand be zero in division:", op1, "/", op2)
            res = op1 / op2
        case '^':
            res = op1 ** op2
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
            if operation != '!':
                if isinstance(op1, float):
                    raise ExpressionException("Factorial can't have a float as an operand")
                elif op1 < 0:
                    raise ExpressionException("Can't calculate a factorial on a negative number")
            res = factorial(op1)
        case '#':
            res = count(op1)
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
    if (op1 is None or op2 is None) and operation != '-' and operation != '~' and operation != '!':
        raise SyntaxException("Operation is not acceptable, you need the two operands to be other than none... "
                              "\nExpression:", op1, operation, op2, "\nRight Syntax: x", operation, "y")
    if (op1 is None or op2 is not None) and operation == '~':
        raise SyntaxException("Operation is not acceptable, in ~ operation, you need the first operand to be none "
                              "and the second one needs to be other than none... \nRight syntax:", operation, "x")
    if op2 is None and operation == '-':
        raise SyntaxException("Operation is not acceptable, in - operation, you need the first operand to be none "
                              "and the second one needs to be other than none... "
                              "\nRight syntax:", operation, "x or: x", operation, "y")
    if op2 is not None and operation == '!':
        raise SyntaxException("Operation is not acceptable, in ! operation, you need the second operand to be "
                              "none... \nExpression:", op1, operation, op2)
    return True


def is_operator(ch):
    """
    Checks if char given is in operators list
    :param ch: the char in check
    :return: True if char given is in operators list, else False.
    """
    return ch in operators
