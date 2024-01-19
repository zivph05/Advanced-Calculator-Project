from exceptions import SyntaxException
from operators import is_operator, op_type, rep
from expression_parser import ExpressionParser


class ValidityCheck:

    def __init__(self, expression: str):
        """
        Validity Check - checks if the expression is valid.
        :param expression: expression given to the program by the user
        :raises: if expression has nothing
        """
        if expression == "":
            raise SyntaxException("Nothing Entered...")
        self.expression = expression

    def make_valid_list(self) -> list:
        """
        Checks if the expression is valid and creates list from the expression
        :return: list of the expression
        :raises: if the check functions found an error...
        """
        try:
            tilda_and_unary_check(self.expression)
            parser = ExpressionParser(self.expression)
            expression_lst = parser.turn_into_list()
            check_list(expression_lst)
        except SyntaxException:
            raise
        return expression_lst


def parentheses_check(expression, index, parentheses_count):
    """
     Checks if the parentheses that is currently watched by the function 'check_list' is valid
    :param expression: the list of the expression given by the user
    :param index: the current parentheses that is being watched
    :param parentheses_count: the current amount of parentheses
    :raises: if parentheses has nothing between them
             if a number is near '(' from the left or a number to the right of ')'
             if in the current location there are more closing parentheses than opening
    """
    item = expression[index]
    if item == '(':
        if (index + 1) < len(expression):
            new_item = expression[index + 1]
            if new_item == ')':
                raise SyntaxException("You can't have a parentheses expression with nothing in between...")
        if (index - 1) >= 0:
            new_item = expression[index - 1]
            if not (is_operator(new_item) or new_item == '('):
                raise SyntaxException("You can't have a number and parentheses with nothing in between...")
        return 1
    elif item == ')':
        if parentheses_count == 0:
            raise SyntaxException("You can't have a closing parentheses without opening first")
        if (index + 1) < len(expression):
            new_ch = expression[index + 1]
            if not (is_operator(new_ch) or new_ch == ')'):
                raise SyntaxException("You can't have a number and parentheses with nothing in between...")
        return -1


def tilda_and_unary_check(expression):
    """
    Runs on string, if found a unary minus or a neg(~) expression then check if it's valid
    :param expression: Expression given by user
    :raises:  if '~' or unary minus is not followed by a unary minus or an expression
    """
    for index in range(0, len(expression)):
        ch = expression[index]
        unary = False
        if ch == '-':
            if index != 0:
                ch_before = expression[index - 1]
                if (ch_before == '(') or (is_operator(ch_before) and op_type(ch_before) != 'l'):
                    unary = True
            else:
                unary = True
        if expression[index] == '~' or unary:
            done = False
            index += 1
            while index < len(expression) and not done:
                if (is_operator(expression[index]) and expression[index] != '-') or expression[index] == ')':
                    if unary:
                        raise SyntaxException("In unary - action, you need to have only an expression"
                                              "or another unary minus")
                    raise SyntaxException("In ~ action, you need to have only an expression"
                                          "or an unary minus")
                elif expression[index] == '(' or '0' <= expression[index] <= '9':
                    done = True
                index += 1


def check_list(expression):
    """
    Runs on list, looks into every item, if it needs a check, goes to the correlated check.
    :param expression: the list of the expression
    :raises: if an item is a dot, no dot needs to be alone, only near 2 numbers.
             if there are more opening parentheses than closing ones
             if the correlated checks have found an error
    """
    parentheses_count = 0
    if not expression:
        return False
    for index in range(0, len(expression)):
        item = expression[index]
        if isinstance(item, str) and item in "()":
            try:
                parentheses_count += parentheses_check(expression, index, parentheses_count)
            except SyntaxException:
                raise
        if item == '.':
            raise SyntaxException("You can only have one dot between two numbers...")
        elif is_operator(item) and item not in rep:
            try:
                check_operator(expression, index)
            except SyntaxException:
                raise
    if parentheses_count != 0:
        raise SyntaxException("You can't open a parentheses without closing!")


def check_operator(expression, index):
    """
    Checks the current expression that is being inspected by the 'check_list' function...
    With acknowledgement to the operator's orientation type
    :param expression: the expression list given by the user
    :param index: current location of the item under inspection
    :raises: if the correlated operator check found an error
    """
    item = expression[index]
    try:
        if op_type(item) == 'l':
            check_l_op(expression, index)
        elif op_type(item) == 'r':
            check_r_op(expression, index)
        else:
            check_m_op(expression, index)
    except SyntaxException:
        raise


def check_l_op(expression, index):
    """
    Checks if the left operation that is currently watched by the function 'check_list' is valid
    :param expression: the list of the expression given by the user
    :param index: the current operation that is being watched
    :raises: if operation is alone - no expression
             if left side doesn't have an expression near it or another operation with orientation that is right
             if right side has an expression near it or another operation with orientation to the right
    """
    index_1 = index - 1
    index_2 = index + 1
    if index_1 < 0:
        raise SyntaxException(f"In {expression[index]} expression - the right syntax is x{expression[index]}")

    item_1 = expression[index_1]

    if not (item_1 == ')' or (is_operator(item_1) and op_type(item_1) != 'r') or isinstance(item_1, (int, float))):
        raise SyntaxException(f"In {expression[index]} expression - there has to be an expression on the left side or "
                              f"another operation with orientation other than right - the right syntax is "
                              f"x{expression[index]}")

    if index_2 < len(expression):
        item_2 = expression[index_2]
        if not ((is_operator(item_2) and op_type(item_2) != 'r') or item_2 == ')'):
            raise SyntaxException(f"In {expression[index]} expression - there has to be no expression on the right side"
                                  f"and no operation with an orientation that to the right "
                                  f"- the right syntax is x{expression[index]}")


def check_r_op(expression, index):
    """
    Checks if the right operation that is currently watched by the function 'check_list' is valid
    :param expression: the list of the expression given by the user
    :param index: the current operation that is being watched
    :raises: if there is no
    """
    index_1 = index - 1
    index_2 = index + 1
    if index_2 >= len(expression):
        raise SyntaxException(f"In {expression[index]} operation - you need to have an expression to the right - "
                              f"Right syntax - {expression[index]} x")

    item_2 = expression[index_2]

    if not (item_2 == '(' or (is_operator(item_2) and op_type(item_2) != 'm') or isinstance(item_2, (int, float))):
        raise SyntaxException(f"In the right side of {expression[index]} operation - you need to have an expression to "
                              f"the right, and no operation that has an orientation other than middle - "
                              f"Right syntax - {expression[index]} x")

    if index_1 >= 0:
        item_1 = expression[index_1]
        if not ((is_operator(item_1) and op_type(item_1) != 'l') or item_1 == '('):
            raise SyntaxException(f"In the right side of {expression[index]} operation - you need to have an "
                                  f"expression to the right, and no operation that has an orientation other than "
                                  f"left - Right syntax - {expression[index]} x")


def check_m_op(expression, index):
    """
    Checks if the right operation that is currently watched by the function 'check_list' is valid
    :param expression: the list of the expression given by the user
    :param index: the current operation that is being watched
    :raises: if there is no expression on one or both sides of the operation
             if there is no expression on the left side or an operation other than left orientating
             if there is no expression on the right side or an operation other than right orientating
    """
    index_1 = index - 1
    index_2 = index + 1
    if index_1 < 0 or index_2 >= len(expression):
        raise SyntaxException(f"In {expression[index]} operation - you need to have two expressions in each side - "
                              f"Right syntax - x {expression[index]} y")
    item_1 = expression[index_1]
    item_2 = expression[index_2]
    if not (item_1 == ')' or (is_operator(item_1) and op_type(item_1) == 'l') or isinstance(item_1, int) or
            isinstance(item_1, float)):
        raise SyntaxException(f"In the left side of {expression[index]} operation - you need to have two expressions "
                              f"and no operation other than left orientation - Right syntax - x {expression[index]} y")

    if not (item_2 == '(' or (is_operator(item_2) and op_type(item_2) == 'r') or isinstance(item_2, int) or
            isinstance(item_2, float)):
        raise SyntaxException(f"In the left side of {expression[index]} operation - you need to have two expressions "
                              f"and no operation other than right orientation - Right syntax - x {expression[index]} y")
