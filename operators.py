from math import pow


class Operator:
    def __init__(self, power, orientation: str):
        """
        Operator - a symbol which represents an action.
        Creates operator
        :param power: the priority of the operator
        :param orientation: the orientation of the operator
        """
        self.importance = power
        self.orientation_of_op = orientation

    def get_importance(self):
        """
        gets the priority of current operator.
        :return: the priority of current operator
        """
        return self.importance

    def get_orientation(self) -> str:
        """
        gets the orientation of current operator.
        :return: the orientation of current operator
        """
        return self.orientation_of_op


"""
    :OPERATORS: A dict containing the operators, symbol is the key of the operator, 
    the value is the Operator class mentioned above
    
    :REP: A list of the characters that the system replaces...
"""
operators = {'+': Operator(1, 'm'),
             '-': Operator(1, 'm'),
             '*': Operator(2, 'm'),
             '/': Operator(2, 'm'),
             '^': Operator(3, 'm'),
             '_': Operator(3.5, 'r'),
             '%': Operator(4, 'm'),
             '@': Operator(5, 'm'),
             '$': Operator(5, 'm'),
             '&': Operator(5, 'm'),
             '~': Operator(6, 'r'),
             '!': Operator(6, 'l'),
             '#': Operator(6, 'l'),
             'u': Operator(7, 'r')}
rep = ['_', 'u']


def count(operand):
    """
    Sums up each digit in a number, before or after a decimal point, if number is too big, returns inf
    :param operand:
    :return:
    """
    if operand == float('inf'):
        return float('inf')

    res = 0
    str_op = str(operand)
    split_num = str_op.split('.')
    for index in range(0, len(split_num)):
        for index_1 in range(0, len(split_num[index])):
            digit = split_num[index][index_1]
            res += int(digit)
    return res


def factorial(operand):
    """
    Calculates the factorial of a number (operand!), if number is too big, returns inf
    :param operand: the number in calculation
    :return: the factorial of op (operand!)
    """
    res = 1
    if operand == float('inf') or operand >= 10000:
        return float('inf')

    operand_int = int(operand)
    for i in range(2, operand_int + 1):
        res *= i
    return res


def mean(op1, op2):
    """
    Calculates the mean of op1 of op2 (op1 @ op2) (op = short for operand!)
    :param op1: the first number in the mean
    :param op2: the second number in the mean.
    :return: Mean of op1 and op2 (op1 @ op2)
    """
    return (op1 + op2) / 2


def calculate(op1, op2, operation: str):
    """
    Calculates the ex. that is given
    :param op1: the first operand
    :param op2: the second operand
    :param operation: the operation
    :return: result of the ex. (op1 ___ op2)
    :raises: if in ! operation has a float value or a negative number
             if in / or in % operation there is a 0 in the 'denominator'
             if in ^ operation op1 is a negative number and (-1 < op2 < 1 and op2 is not 0) or,
             if in ^ operation op1 and op2 are 0
             if in # operation op1 is a negative number
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
            try:
                res = round(op1 / op2, 10)
            except ZeroDivisionError:
                raise
        case '^':
            if op1 < 0 and (-1 < op2 < 1) and op2 != 0:
                raise ArithmeticError("Can't have a negative number be in root of (when the second op is between "
                                      "1 and -1 and not zero)")
            if op1 == 0 and op2 < 1:
                raise ArithmeticError("Can't have a 0 in power of a number smaller than 1")
            try:
                res = pow(op1, op2)
            except OverflowError:
                res = float('inf')
        case '%':
            try:
                res = round(op1 % op2, 10)
            except ZeroDivisionError:
                raise
        case '~':
            res = -op2
        case '@':
            res = round(mean(op1, op2), 10)
        case '$':
            res = max(op1, op2)
        case '&':
            res = min(op1, op2)
        case '!':
            if (op1 % 1) != 0 and op1 != float('inf'):
                raise ArithmeticError("Factorial can't have a float as an operand")
            elif op1 < 0:
                raise ArithmeticError("Can't calculate a factorial on a negative number")
            res = factorial(op1)
        case '#':
            if op1 < 0:
                raise ArithmeticError("Can't calculate a counting expression on a negative number")
            res = count(op1)
        case 'u':
            res = -op2
        case '_':
            res = -op2
    return res


def priority(op: str):
    """
    Gives the "power of" the operation given
    :param op: the operation that is being evaluated
    :return: the power of the operation given
    """
    return operators.get(op).get_importance()


def op_type(op: str) -> str:
    """
    Checks what is the orientation type of the operator.
    :param op: the operator in check
    :return: The orientation type of the operator
    """
    return operators.get(op).get_orientation()


def is_operator(ch: str) -> bool:
    """
    Checks if char given is in operators list
    :param ch: the char in check
    :return: True if char given is in operators list, else False.
    """
    return ch in operators
