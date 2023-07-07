from typing import Optional

from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.exception.lexical_analyzer_exception import LexicalAnalyzerException
from analyzer.lexical.lexical.v1.identifier_lexical import IdentifierLexical
from analyzer.lexical.lexical.v1.space_lexical import SpaceLexical
from analyzer.lexical.lexical.v1.underscore_lexical import UnderscoreLexical
from analyzer.lexical.model.token import TokenModel


class LexicalAnalyzer:
    """
    The lexical analyzer class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'LexicalAnalyzer' class.
        """
        self.__lexical: list[AutomatonLexical] = [SpaceLexical(), IdentifierLexical(), UnderscoreLexical()]

    def analyse(self, command: str) -> list[TokenModel]:
        """
        Analyze the command for extract a token list.
        :param command: The command to analyze.
        :return: The token list for analyzing of the command.
        """
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
        """
        Extract a token.
        :param characters: The command convert in the character list.
        :param character_position: The position of the analyzer.
        :param character_maximum: The ma
        :return: A token model instance or None.
        """
        lexical_index: int = 0
        token: Optional[TokenModel] = None
        lexical_maximum: int = len(self.__lexical)

        while lexical_index.__lt__(lexical_maximum) and token is None:
            token = self.__lexical[lexical_index].extract_token(characters, character_position, character_maximum)
            lexical_index += 1

        return token
