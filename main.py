from analyzer.core.exception.interpreter_exception import InterpreterException
from interpreter import Interpreter

try:
    interpreter: Interpreter = Interpreter()
    print("> ", end='')
    interpreter.interpret(input())
except InterpreterException as e:
    print(str(e))
