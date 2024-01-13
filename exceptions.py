class ExpressionException(Exception):
    def __init__(self, message):
        self.message = message


class SyntaxException(Exception):
    def __init__(self, message):
        self.message = message
