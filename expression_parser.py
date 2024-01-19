from exceptions import SyntaxException
from operators import is_operator, op_type, rep


class ExpressionParser:
    def __init__(self, expression: str):
        """
        Expression Parser - breaks down the string into recognizable numbers and operators
        puts the expression from the user into it's attributes
        :param expression: expression that the user inputs
        """
        self.expression = expression

    def turn_into_list(self) -> list:
        """
        Calls function that turns expression into a list to and returns it for classes that use the parser
        :return: a list which contains the expression, numbers are numeric values
        :raises: if 'expression_to_lst' found an error
        """
        try:
            return expression_to_lst(self.expression)
        except SyntaxException:
            raise


def expression_to_lst(expression: str) -> list:
    """
    Turns the expression into a list of items, changes the symbols of unary '-' into symbols that the system recognizes
    as the unary symbols. Inputs the numbers as a real number and not as separate characters with 'make_num' function.
    if unary symbols repeat themselves near each-other, delete.
    :param expression: the input expression that is being turned into the list.
    :return: the expression as a list.
    :raises: if there is a character that is not acceptable(nor operation nor number)
             if 'make_number' identified an error
    """
    output = []
    index = 0
    while index in range(0, len(expression)):
        ch = expression[index]
        if '0' <= ch <= '9':
            try:
                new_index, num = make_num(expression, index)
                output.append(num)
                index = new_index
            except SyntaxException:
                raise
        elif is_operator(ch) and ch not in rep:
            if ch == '-':
                if output and (output[-1] == 'u' or output[-1] == '_'):
                    output.pop()
                elif output and is_operator(output[-1]) and op_type(output[-1]) != 'l':
                    output.append('u')
                elif not output or output[-1] == '(':
                    output.append('_')
                else:
                    output.append('-')
            else:
                output.append(ch)
            index += 1
        else:
            if ch not in ".()":
                raise SyntaxException("Unidentified character")
            output.append(ch)
            index += 1
    return output


def make_num(expression: str, index: int):
    """
    Turns the current number that is being scanned by 'expression_to_lst' function
    from separate characters into a number, either with or without a decimal point.
    :param expression: the expression that is being scanned
    :param index: the current index of the expression that needs to turn into a number
    :returns: the index after scanning the number and the number as a numeric value
    :raises: if there is a decimal point more than once in the number scanned
    """
    ch = expression[index]
    num = 0
    dot = 0.0
    after_dot = False
    while index < len(expression) and ch in "0123456789.":
        if ch == '.':
            if after_dot:
                raise SyntaxException("A dot needs to be between 2 numbers...")
            after_dot = True
        elif after_dot:
            digit = int(ch)
            dot = dot * 10 + digit
        else:
            digit = int(ch)
            num = num * 10 + digit
        index += 1
        if index < len(expression):
            ch = expression[index]
    if after_dot:
        while dot > 1:
            dot /= 10
        num += dot
    return index, num
