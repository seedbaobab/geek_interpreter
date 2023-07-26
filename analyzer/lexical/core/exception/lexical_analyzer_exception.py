from analyzer.core.exception.interpreter_exception import InterpreterException


class LexicalAnalyzerException(InterpreterException):

    def __init__(self, message: str):
        super().__init__(message)
