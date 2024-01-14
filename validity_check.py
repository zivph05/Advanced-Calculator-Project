from exceptions import SyntaxException
from operators import is_operator, op_type, rep


def check(expression):
    if not check_line(expression):
        return False
    if not parentheses_check(expression):
        return False
    # if not tilda_check(expression):
        # print('tilda')
        # return False
    return True


def parentheses_check(expression):
    stack = []
    for index in range(0, len(expression)):
        ch = expression[index]
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            stack.pop()
    if stack:
        return False
    return True


def tilda_check(expression):
    for index in range(0, len(expression)):
        ch = expression[index]
        if expression[index] == '~':
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
    for index in range(0, len(expression)):
        ch = expression[index]
        if not ('0' <= ch <= '9' or (is_operator(ch) and ch not in rep) or ch == ')' or ch == '('):
            return False
    return True


def go(lst):
    for index in range(0, len(lst)):
        item = lst[index]
        if is_operator(item) and op_type(item) == 'm':
            index_1 = index - 1
            index_2 = index + 1
            if index_1 < 0 or index_2 >= len(lst):
                return False

            item_1 = lst[index_1]
            item_2 = lst[index_2]
    return True


def main():
    ex = "(12+6)-(--(-5)&--1)"
    print(check(ex))


if __name__ == "__main__":
    main()
