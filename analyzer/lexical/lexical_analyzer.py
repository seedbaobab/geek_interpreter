from typing import Optional

from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.exception.lexical_analyzer_exception import LexicalAnalyzerException
from analyzer.lexical.lexical.v1.close_parenthesis_lexical import CloseParenthesisLexical
from analyzer.lexical.lexical.v1.comma_lexical import CommaLexical
from analyzer.lexical.lexical.v1.identifier_lexical import IdentifierLexical
from analyzer.lexical.lexical.v1.integer_lexical import IntegerLexical
from analyzer.lexical.lexical.v1.open_parenthesis_lexical import OpenParenthesisLexical
from analyzer.lexical.lexical.v1.point_lexical import PointLexical
from analyzer.lexical.lexical.v1.space_lexical import SpaceLexical
from analyzer.lexical.lexical.v1.string_lexical import StringLexical
from analyzer.lexical.model.token import TokenModel


class LexicalAnalyzer:

    def __init__(self):
        self.__lexical: list[AutomatonLexical] = [SpaceLexical(), PointLexical(), OpenParenthesisLexical(),
                                                  CloseParenthesisLexical(), CommaLexical(), IdentifierLexical(),
                                                  IntegerLexical(), StringLexical()]

    def analyse(self, command: str):
        character_position: int = 0
        characters: list[str] = [*command]
        character_maximum: int = len(characters)
        tokens: list[TokenModel] = []
        forward: bool = True

        while character_position.__lt__(character_maximum) and forward:
            token: Optional[TokenModel] = self.__extract_token(characters, character_position, character_maximum)
            if token is not None:
                character_position += token.size
                if token.typology.__ne__("SPACE"):
                    tokens.append(token)
            else:
                forward = False

        if not forward:
            message: str = "You have an error on your command here : "
            space: str = "{0}^".format("".ljust(len(message) + character_position, " "))
            raise LexicalAnalyzerException("{0}{1}\n{2}".format(message, command, space))

        return tokens

    def __extract_token(self, characters: list[str], character_position: int, character_maximum: int) \
            -> Optional[TokenModel]:
        lexical_index: int = 0
        token: Optional[TokenModel] = None
        lexical_maximum: int = len(self.__lexical)

        while lexical_index.__lt__(lexical_maximum) and token is None:
            token = self.__lexical[lexical_index].extract_token(characters, character_position, character_maximum)
            lexical_index += 1

        print("ANALYZER EXTRACTION QUIT")
        return token
