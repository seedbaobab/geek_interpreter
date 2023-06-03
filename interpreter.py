from analyser.lexical_analyser.lexical.model.token_model import TokenModel
from analyser.lexical_analyser.lexical_analyser import LexicalAnalyser


class Interpreter:

    def __init__(self):
        self.__lexical_analyser: LexicalAnalyser = LexicalAnalyser()

    def interpret(self, command: str):
        tokens: list[TokenModel] = self.__lexical_analyser.analyse(command)
        for token in tokens:
            print(token.to_str())
