from __future__ import annotations

from abc import abstractmethod, ABC

from analyser.lexical_analyser.core.automaton.automaton_state import AutomatonState
from analyser.lexical_analyser.lexical.model.token_model import TokenModel


class AutomatonLexical(ABC):

    def __init__(self, typology: str):
        self._source_state: AutomatonState | None = None
        self.__typology: str = typology
        self._initialize()

    @property
    def typology(self):
        return self.__typology

    @property
    def source_state(self):
        return self._source_state

    @source_state.setter
    def source_state(self, source_state: AutomatonState):
        self._source_state = source_state

    @abstractmethod
    def _initialize(self):
        pass

    def extract_token(self, character: list[str], position: int = 0) -> tuple[TokenModel | None, int]:
        (success, token, new_position) = self._source_state.get_token(character, position, len(character))
        return (TokenModel(self.__typology, token, position, new_position), new_position) if success else (None, position)
