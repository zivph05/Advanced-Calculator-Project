from binary_tree import TreeNode
from exceptions import SyntaxException
from operators import is_operator, op_type, priority, calculate
from validity_check import ValidityCheck


class ExpressionSolver:
    def __init__(self, expression):
        """
        Expression Solver - Solves the expression.
        Creates solver and checks if expression is valid with Validity Check Class
        :param expression: the expression in check
        :raises: if Validity Check has found an error...
        """
        exp = expression.replace(" ", "")
        exp = exp.replace("\n", "")
        exp = exp.replace("\t", "")

        check = ValidityCheck(exp)
        try:
            self.expression_lst = check.make_valid_list()
        except SyntaxException:
            raise

    def solve(self):
        """
        Solves the expression, creates a postfix expression from list, creates tree and calculates...
        :return: A numeric value of the solution of the expression
        """
        post = turn_to_postfix(self.expression_lst)
        tree = create_tree(post)
        try:
            return calc_expression(tree)
        except ZeroDivisionError:
            raise
        except ArithmeticError:
            raise


def create_tree(postfix_expression: list) -> TreeNode:
    """
    Creates a Binary tree with class 'TreeNode', in the tree there will be the expression with acknowledgement of the
    priority of each part of the expression.
    :param postfix_expression: The expression given to the program with use of the 'expression_to_postfix' function
    :return: The expression in a binary tree
    """
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


def turn_to_postfix(expression: list) -> list:
    """
    Turns the expression given in a postfix expression
    :param expression: The expression given to the function after turning into a list with use of 'expression_to_lst'
    function activated from ValidityCheck Class
    :return: The list in a postfix orientation
    """
    postfix = []
    operator_stack = []

    for index in range(0, len(expression)):
        item = expression[index]
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


def calc_expression(root: TreeNode):
    """
    Scanning the binary tree given by the 'make_tree' function and
    with use of the 'calculate' function from operators module returns the numeric value of the expression.
    :param root: The binary tree with the expression
    :return: The numeric value of the expression
    :raises: if 'Calculate' function has identified an error
    """
    if not root:
        return None
    if root.is_leaf() and not is_operator(root.data):
        return root.data

    try:
        left = calc_expression(root.left)
        right = calc_expression(root.right)
        return calculate(left, right, root.data)
    except ZeroDivisionError:
        raise
    except ArithmeticError:
        raise
