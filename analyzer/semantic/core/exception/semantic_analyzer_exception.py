from analyzer.core.exception.interpreter_exception import InterpreterException


class SemanticAnalyzerException(InterpreterException):
    """
    Custom Exception for semantic exception.
    """

    def __init__(self, message: str):
        """
        Initialize a new instance of 'SemanticAnalyzerException' class.
        :param message: The message of the exception.
        """
        super().__init__(message)
