from typing import Optional

from analyser.lexical_analyser.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyser.lexical_analyser.model.token import TokenModel


class AutomatonLexical:

    def __init__(self):
        self._source: Optional[AutomatonStateLexical] = None

    def extract_token(self, characters: list[str], position: int, max_position: int) -> Optional[TokenModel]:
        (success, end, token) = self._source.extract_token(characters, position, max_position)
        return TokenModel(token, position, end) if success else None
