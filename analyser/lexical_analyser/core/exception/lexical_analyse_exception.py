from analyser.core.interpreter_exception import InterpreterException


class LexicalAnalyseException(InterpreterException):

    def __init__(self, message: str):
        super().__init__(message)
