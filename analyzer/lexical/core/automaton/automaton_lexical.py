from abc import ABC, abstractmethod
from typing import Optional

from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.model.token import TokenModel


class AutomatonLexical(ABC):

    def __init__(self, typology: str):
        self.__source_state: Optional[AutomatonStateLexical] = None
        self.__typology: str = typology
        self._init()

    @property
    def source_state(self):
        return self.__source_state

    @source_state.setter
    def source_state(self, value: AutomatonStateLexical):
        self.__source_state = value

    @property
    def typology(self) -> str:
        return self.__typology

    def extract_token(self, characters: list[str], position: int, max_position: int) -> Optional[TokenModel]:
        (success, end, token) = self.__source_state.extract_token(characters, position, max_position)
        return TokenModel(self.__typology, token, position, end) if success else None

    @abstractmethod
    def _init(self):
        """
        Initialize the lexical unit.
        """
        pass
