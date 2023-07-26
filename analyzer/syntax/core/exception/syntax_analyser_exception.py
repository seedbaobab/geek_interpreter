from analyzer.core.exception.interpreter_exception import InterpreterException


class SyntaxAnalyzerException(InterpreterException):
    """
    Custom exception for syntax error.
    """

    def __init__(self, message: str):
        """
        Initialize a new instance of 'SyntaxAnalyzerException' class.
        :param message: The message exception.
        """
        super().__init__(message)
