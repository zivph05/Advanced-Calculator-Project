from binary_tree import TreeNode
from exceptions import ExpressionException
from operators import is_operator, priority, op_type, calculate


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
                t.right = stack.pop()
            elif type_operator == 'l':
                t.left = stack.pop()
            else:
                t.right = stack.pop()
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
    in_num = False
    in_min_exp = False
    output = []
    num = 0
    for index in range(0, len(expression)):
        ch = expression[index]
        if '0' <= ch <= '9':
            in_num = True
        else:
            if not in_num:
                if ch == '-':
                    if in_min_exp:
                        output.pop()
                        output.pop()
                        in_min_exp = False
                    elif output and output[-1] != ')':
                        output.append('(')
                        output.append('u')
                        in_min_exp = True
                    else:
                        in_min_exp = False
                        output.append('u')
                else:
                    in_min_exp = False
                    output.append(ch)
            if in_num:
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
    if root.is_leaf():
        return root.data

    left = do(root.left)
    right = do(root.right)

    try:
        return calculate(left, right, root.data)
    except ExpressionException as e:
        print(e)


def main():
    a = "2+--3!"
    inorder(create_tree(turn_to_postfix(expression_to_lst(a))))
    print("output: ", do(create_tree(turn_to_postfix(expression_to_lst(a)))))


if __name__ == "__main__":
    main()
