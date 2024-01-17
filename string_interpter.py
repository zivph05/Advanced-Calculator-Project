from binary_tree import TreeNode
from exceptions import ExpressionException, SyntaxException
from operators import is_operator, priority, op_type, calculate, rep
from validity_check import check, check_list


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def create_tree(postfix_expression):
    stack = []
    for item in postfix_expression:
        t = TreeNode(item)
        if isinstance(item, str) and is_operator(item):
            type_operator = op_type(item)
            if type_operator == 'r':
                if stack:
                    t.right = stack.pop()
            elif type_operator == 'l':
                if stack:
                    t.left = stack.pop()
            else:
                if stack:
                    t.right = stack.pop()
                if stack:
                    t.left = stack.pop()
        stack.append(t)

    return stack.pop()


# turn to list, make list postfix, take postfix and calc
def turn_to_postfix(expression):
    postfix = []
    operator_stack = []
    # run on expression, while in expression, put into stack
    # on end, put in postfix

    for index in range(0, len(expression)):
        item = expression[index]
        # if number is not  in
        if not is_operator(item) and item != '(' and item != ')':
            postfix.append(item)
        elif item == '(':
            operator_stack.append(item)
        elif item == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix.append(operator_stack.pop())
            operator_stack.pop()
        elif is_operator(item):
            while operator_stack and operator_stack[-1] != '(' and priority(operator_stack[-1]) >= priority(item):
                postfix.append(operator_stack.pop())
            operator_stack.append(item)

    while operator_stack:
        postfix += operator_stack.pop()
    return postfix


def expression_to_lst(expression):
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
                # unary?
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


def make_num(expression, index):
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


def do(root):
    if not root:
        return None
    if root.is_leaf() and not is_operator(root.data):
        return root.data

    try:
        left = do(root.left)
        right = do(root.right)
        return calculate(left, right, root.data)
    except ExpressionException:
        raise
    except SyntaxException:
        raise
    except ZeroDivisionError:
        raise


def main():
    try:
        a = input("Enter an expression: ")
    except EOFError:
        print("EOF, Ending Program...")
        return
    exp = a.replace(" ", "")
    exp = a.replace("\n", "")
    exp = a.replace("\t", "")

    try:
        check(exp)
        lst = expression_to_lst(exp)
        check_list(lst)
        inorder(create_tree(turn_to_postfix(lst)))
        print("output: ", do(create_tree(turn_to_postfix(lst))))
    except ExpressionException as e:
        print(e)
    except SyntaxException as e:
        print(e)
    except ZeroDivisionError as e:
        print("Error! ", e)

        # _ after ( after start, u and _ cant be before operation


if __name__ == "__main__":
    main()
