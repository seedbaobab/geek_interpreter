from abc import ABC, abstractmethod
from typing import Optional

from analyzer.core.typology.typology import Typology
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.token.token import TokenModel


class AutomatonLexical(ABC):
    """
    Automaton for recognize lexical unit.
    """

    def __init__(self, typology: Typology):
        """
        Initialize a new instance of 'AutomatonLexical' class.
        :param typology: The automaton typology.
        """
        self.__source_state: Optional[AutomatonStateLexical] = None
        self.__typology: Typology = typology
        self._init()

    @property
    def source_state(self):
        """
        Get the source state of the automaton.
        :return: The source state of the automaton.
        """
        return self.__source_state

    @source_state.setter
    def source_state(self, value: AutomatonStateLexical):
        """
        Set the source state of the automaton.
        :param value: The new value of the source state of the automaton.
        """
        self.__source_state = value

    @property
    def typology(self) -> str:
        """
        Get the automaton typology.
        :return:
        """
        return self.__typology.value

    def extract_token(self, characters: list[str], position: int, max_position: int) -> Optional[TokenModel]:
        """
        Extract a lexical unit token.
        :param characters: The command in character list.
        :param position: The lexical analyzer position in the list of characters.
        :param max_position: The position maximum the lexical analyzer can reach.
        :return: None if no lexical unit can be extracted or a TokenModel.
        """
        (success, end, token) = self.__source_state.extract_token(characters, position, max_position)
        return TokenModel(self.__typology, token, position, end) if success else None

    @abstractmethod
    def _init(self):
        """
        Initialize the lexical unit.
        """
        pass
