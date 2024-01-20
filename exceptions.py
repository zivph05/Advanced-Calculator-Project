class SyntaxException(Exception):
    def __init__(self, message):
        """
        Syntax exception - raised when the expression is incorrect in the syntax
        Creates the exception
        :param message: The correlated message given by the System
        """
        self.message = message
