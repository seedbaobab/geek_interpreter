from analyzer.lexical.lexical_analyzer import LexicalAnalyzer
from analyzer.lexical.model.token import TokenModel


class Interpreter:

    def __init__(self):
        self.__lexical_analyser: LexicalAnalyzer = LexicalAnalyzer()

    def interpret(self, command: str):
        print(command)
        tokens: list[TokenModel] = self.__lexical_analyser.analyse(command)
        for token in tokens:
            print(token.to_str())
