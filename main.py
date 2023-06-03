import sys

from analyser.core.interpreter_exception import InterpreterException
from interpreter import Interpreter

try:
    interpreter: Interpreter = Interpreter()
    interpreter.interpret("api.controller.method(123, \"arg1\")")
except InterpreterException as e:
    print(str(e))
