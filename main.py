from exceptions import SyntaxException
from solve_expression import ExpressionSolver


def main():
    while True:
        try:
            expression = input("Enter an expression: ")
        except EOFError:
            print("EOF, Ending Program...")
            return
        exp = expression.replace(" ", "")
        exp = exp.replace("\n", "")
        exp = exp.replace("\t", "")

        try:
            solver = ExpressionSolver(exp)
            print(solver.solve())
        except SyntaxException as e:
            print("Error in syntax!", e)
        except ZeroDivisionError as e:
            print("Zero denominator error while solving expression!", e)
        except ArithmeticError as e:
            print("Arithmetic error while solving expression!", e)


if __name__ == "__main__":
    main()
