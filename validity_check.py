from exceptions import SyntaxException
from operators import is_operator, op_type, rep

def check(expression):
    try:
        if not tilda_check(expression):
            print('tilda')
            raise SyntaxException("~~TILDA!!~~")
    except SyntaxException:
        raise
    return True


def parentheses_check(expression, index, parentheses_count):
    item = expression[index]
    if item == '(':
        if (index + 1) < len(expression):
            new_item = expression[index + 1]
            if new_item == ')':
                raise SyntaxException("You can't have a parenthesrs expression with nothing in between...")
        if (index - 1) >= 0:
            new_item = expression[index - 1]
            if not (is_operator(new_item) or new_item == '('):
                raise SyntaxException("You can't have a number and parenthesrs with nothing in between...")
        return 1
    elif item == ')':
        if parentheses_count == 0:
            raise SyntaxException("You can't have a closing parentheses without opening first")
        if (index + 1) < len(expression):
            new_ch = expression[index + 1]
            if not (is_operator(new_ch) or new_ch == ')'):
                raise SyntaxException("You can't have a number and parentheses with nothing in between...")
        return -1


def tilda_check(expression):
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
            flag = True
            done = False
            index += 1
            while index < len(expression) and flag and not done:
                if (is_operator(expression[index]) and expression[index] != '-') or expression[index] == ')':
                    flag = False
                elif expression[index] == '(' or '0' <= expression[index] <= '9':
                    done = True
                index += 1
            if not flag:
                return False
    return True


def check_list(expression):
    parentheses_count = 0
    if expression == []:
        return False
    for index in range(0, len(expression)):
        item = expression[index]
        if isinstance(item,str) and item in "()":
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
    return True


def check_operator(expression, index):
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
    index_1 = index - 1
    index_2 = index + 1
    if index_1 < 0:
        raise SyntaxException("Left error - None Exists")

    item_1 = expression[index_1]

    if not (item_1 == ')' or (is_operator(item_1) and op_type(item_1) != 'r') or isinstance(item_1, int) or
            isinstance(item_1, float)):
        raise SyntaxException("Left error - Side 1")

    if index_2 < len(expression):
        item_2 = expression[index_2]
        if not ((is_operator(item_2) and op_type(item_2) != 'r') or item_2 == ')'):
            raise SyntaxException("Left error - Side 2")


def check_r_op(expression, index):
    index_1 = index - 1
    index_2 = index + 1
    if index_2 >= len(expression):
        raise SyntaxException("Right error - None Exists")

    item_2 = expression[index_2]

    if not (item_2 == '(' or (is_operator(item_2) and op_type(item_2) != 'm') or isinstance(item_2, int) or
            isinstance(item_2, float)):
        raise SyntaxException("Right error - Side 1")

    if index_1 >= 0:
        item_1 = expression[index_1]
        if not ((is_operator(item_1) and op_type(item_1) != 'l') or item_1 == '('):
            raise SyntaxException("Right error - Side 2")


"""
def check_dot(expression, index):
    index_1 = index - 1
    index_2 = index + 1
    if index_1 < 0:
        raise SyntaxException("A dot needs to be between 2 numbers...")
    if index_2 >= len(expression):
        raise SyntaxException("A dot needs to be between 2 numbers...")
    ch_b = expression[index_1]
    ch_a = expression[index_2]
    if ch_b not in operands or ch_a not in operands:
        raise SyntaxException("A dot needs to be between 2 numbers...")

"""


def check_m_op(expression, index):
    index_1 = index - 1
    index_2 = index + 1
    if index_1 < 0 or index_2 >= len(expression):
        raise SyntaxException("Middle error - None Exists")
    item_1 = expression[index_1]
    item_2 = expression[index_2]
    if not (item_1 == ')' or (is_operator(item_1) and op_type(item_1) == 'l') or isinstance(item_1, int) or
            isinstance(item_1, float)):
        raise SyntaxException("Middle error - Side 1")

    if not (item_2 == '(' or (is_operator(item_2) and op_type(item_2) == 'r') or isinstance(item_2, int) or
            isinstance(item_2, float)):
        raise SyntaxException("Middle error - Side 2")


def main():
    ex = "(12+6)-(--(-5)&--1)"
    print(check(ex))


if __name__ == "__main__":
    main()
