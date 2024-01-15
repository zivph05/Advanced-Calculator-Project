from exceptions import SyntaxException
from operators import is_operator, op_type, rep


def check(expression):
    if not check_line(expression):
        return False
    if not parentheses_check(expression):
        return False
    if not tilda_check(expression):
        print('tilda')
        return False
    return True


def parentheses_check(expression):
    stack = []
    for index in range(0, len(expression)):
        ch = expression[index]
        if ch == '(':
            if (index + 1) < len(expression):
                new_ch = expression[index + 1]
                if new_ch == ')':
                    return False
            if (index - 1) >= 0:
                new_ch = expression[index - 1]
                if not (is_operator(new_ch) or new_ch == '('):
                    return False
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            if (index + 1) < len(expression):
                new_ch = expression[index + 1]
                if not (is_operator(new_ch) or new_ch == ')'):
                    return False
            stack.pop()
    if stack:
        return False
    return True


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


def check_line(expression):
    if expression == "":
        return False
    for index in range(0, len(expression)):
        ch = expression[index]
        if not ('0' <= ch <= '9' or (is_operator(ch) and ch not in rep) or ch == ')' or ch == '(' or ch == '.'):
            return False
        if ch == '.':
            index_1 = index - 1
            index_2 = index + 1
            if index_1 < 0:
                return False
                # raise SyntaxException("No .")
            if index_2 >= len(expression):
                return False
                # raise SyntaxException("No .")
            ch_b = expression[index_1]
            ch_a = expression[index_2]
            if ch_b not in "0123456789" or ch_a not in "0123456789":
                return False
            # raise SyntaxException("No .")
    return True


def go(lst):
    for index in range(0, len(lst)):
        item = lst[index]
        if is_operator(item):
            if op_type(item) == 'm':
                index_1 = index - 1
                index_2 = index + 1
                if index_1 < 0 or index_2 >= len(lst):
                    raise SyntaxException("Middle error - None Exists")
                item_1 = lst[index_1]
                item_2 = lst[index_2]
                if not (item_1 == ')' or (is_operator(item_1) and op_type(item_1) == 'l') or isinstance(item_1, int) or
                        isinstance(item_1, float)):
                    raise SyntaxException("Middle error - Side 1")

                if not (item_2 == '(' or (is_operator(item_2) and op_type(item_2) == 'r') or isinstance(item_2, int) or
                        isinstance(item_2, float)):
                    raise SyntaxException("Middle error - Side 2")

            elif is_operator(item) and op_type(item) == 'l':
                index_1 = index - 1
                index_2 = index + 1
                if index_1 < 0:
                    raise SyntaxException("Left error - None Exists")

                item_1 = lst[index_1]

                if not (item_1 == ')' or (is_operator(item_1) and op_type(item_1) != 'r') or isinstance(item_1, int) or
                        isinstance(item_1, float)):
                    raise SyntaxException("Left error - Side 1")

                if index_2 < len(lst):
                    item_2 = lst[index_2]
                    if not ((is_operator(item_2) and op_type(item_2) != 'r') or item_2 == ')'):
                        raise SyntaxException("Left error - Side 2")

            else:
                index_1 = index - 1
                index_2 = index + 1
                if index_2 >= len(lst):
                    raise SyntaxException("Right error - None Exists")

                item_2 = lst[index_2]

                if not (item_2 == '(' or (is_operator(item_2) and op_type(item_2) != 'm') or isinstance(item_2, int) or
                        isinstance(item_2, float)):
                    raise SyntaxException("Right error - Side 1")

                if index_1 >= 0:
                    item_1 = lst[index_1]
                    if not ((is_operator(item_1) and op_type(item_1) != 'l') or item_1 == '('):
                        raise SyntaxException("Right error - Side 2")
    return True


def main():
    ex = "(12+6)-(--(-5)&--1)"
    print(check(ex))


if __name__ == "__main__":
    main()
