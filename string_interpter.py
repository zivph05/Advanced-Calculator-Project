from binary_tree import TreeNode
from exceptions import ExpressionException, SyntaxException
from operators import is_operator, priority, op_type, calculate
from validity_check import check, go


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
            while (operator_stack and operator_stack[-1] != '(' and priority(operator_stack[-1]) >= priority(item) and
                   not (operator_stack[-1] == 'u' and item == 'u')):
                postfix.append(operator_stack.pop())
            operator_stack.append(item)

    while operator_stack:
        postfix += operator_stack.pop()
    return postfix


def expression_to_lst(expression):
    in_num = False
    in_min_exp = False
    a = False
    output = []
    num = 0
    for index in range(0, len(expression)):
        ch = expression[index]
        if '0' <= ch <= '9':
            in_num = True
        else:
            if not in_num:
                if ch == '-':
                    # unary?
                    if output and (output[-1] == 'u' or output[-1] == '_'):
                        if in_min_exp:
                            output.pop()
                            in_min_exp = False
                        output.pop()
                    elif output and is_operator(output[-1]):
                        output.append('(')
                        output.append('u')
                        in_min_exp = True
                    elif not output or output[-1] == '(':
                        output.append('_')
                    else:
                        output.append('-')
                else:
                    output.append(ch)
            else:
                output.append(num)
                if in_min_exp:
                    output.append(')')
                    in_min_exp = False
                in_num = False
                num = 0
                output.append(ch)
        if in_num:
            digit = int(ch)
            num = num * 10 + digit

    if in_num:
        output.append(num)
        if in_min_exp:
            output.append(')')

    return output


def do(root):
    if not root:
        return None
    if root.is_leaf() and not is_operator(root.data):
        return root.data

    try:
        left = do(root.left)
        right = do(root.right)
        return calculate(left, right, root.data)
    except ExpressionException as e:
        print(e)
    except SyntaxException as e:
        print(e)


def main():
    try:
        a = input("Enter an expression: ")
    except EOFError:
        print("Keyboard Interrupt, Ending Program...")
        return
    if check(a):
        lst = expression_to_lst(a)
        try:
            go(lst)
            inorder(create_tree(turn_to_postfix(lst)))
            print("output: ", do(create_tree(turn_to_postfix(lst))))
        except ExpressionException as e:
            print(e)
        except SyntaxException as e:
            print(e)
    else:
        print("Not Valid")

        # _ after ( after start, u and _ cant be before operation


if __name__ == "__main__":
    main()
