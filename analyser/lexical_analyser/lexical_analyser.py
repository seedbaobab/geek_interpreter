from __future__ import annotations

from typing import Optional

from analyser.lexical_analyser.core.automaton.automaton_lexical import AutomatonLexical
from analyser.lexical_analyser.core.exception.lexical_analyse_exception import LexicalAnalyseException
from analyser.lexical_analyser.lexical.model.token_model import TokenModel
from analyser.lexical_analyser.lexical.v1.close_parenthsis_lexical import CloseParenthesisLexical
from analyser.lexical_analyser.lexical.v1.comma_lexical import CommaLexical
from analyser.lexical_analyser.lexical.v1.identifier_lexical import IdentifierLexical
from analyser.lexical_analyser.lexical.v1.integer_lexical import IntegerLexical
from analyser.lexical_analyser.lexical.v1.open_parenthsis_lexical import OpenParenthesisLexical
from analyser.lexical_analyser.lexical.v1.space_lexical import SpaceLexical
from analyser.lexical_analyser.lexical.v1.string_lexical import StringLexical
from analyser.lexical_analyser.lexical.v1.point_lexical import PointLexical


class LexicalAnalyser:

    def __init__(self):
        self.__lexical: list[AutomatonLexical] = [IntegerLexical(), IdentifierLexical(), StringLexical(),
                                                  PointLexical(), CloseParenthesisLexical(), SpaceLexical(),
                                                  OpenParenthesisLexical(), CommaLexical()]

    def analyse(self, command: str):
        forward: bool = True
        character_position: int = 0
        characters: list[str] = [*command]
        character_maximum: int = len(characters)
        tokens: list[TokenModel] = []

        while character_position.__lt__(character_maximum) and forward:
            (token, character_position) = self.__get_token(characters, character_position)
            if token is not None:
                if token.typology.__ne__("SPACE"):
                    tokens.append(token)
            else:
                forward = False

        if not forward:
            message: str = "You have an error on your command here : "
            space: str = "{0}^".format("".ljust(len(message) + character_position, " "))
            raise LexicalAnalyseException("{0}{1}\n{2}".format(message, command, space))

        return tokens

    def __get_token(self, characters: list[str], position: int) -> tuple[(Optional[TokenModel]), int]:
        lexical_index: int = 0
        token: TokenModel | None = None
        lexical_maximum: int = len(self.__lexical)
        new_position: int = position

        while lexical_index.__lt__(lexical_maximum) and token is None:
            (token, new_position) = self.__lexical[lexical_index].extract_token(characters, position)
            if token is None:
                lexical_index += 1

        return (None, position) if token is None else (token, new_position)
