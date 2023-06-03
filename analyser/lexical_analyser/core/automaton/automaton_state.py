from __future__ import annotations

from analyser.lexical_analyser.core.automaton.automaton_transition import AutomatonTransition
from analyser.lexical_analyser.core.automaton.i_automaton_state import IAutomatonState


class AutomatonState(IAutomatonState):

    def __init__(self, is_final: bool):
        super().__init__(is_final)
        self.__transitions: list[AutomatonTransition] = []

    def get_token(self, characters: list[str], position: int, maximum_characters: int, token: str = None) -> \
            tuple[bool, str | None, int]:

        if position.__ge__(maximum_characters):
            return (True, token, position) if (self.is_final and token is not None) else (False, None, position)

        forward: bool = False
        index_transition: int = 0
        maximum_transition: int = len(self.__transitions)

        while index_transition.__lt__(maximum_transition) and position.__lt__(maximum_characters) and not forward:
            if self.__transitions[index_transition].is_valid(characters[position]):
                (forward, token_found, new_position) = self.__transitions[index_transition].destination.\
                    get_token(characters, position + 1, maximum_characters, ("" if token is None else token) + characters[position])
                if forward:
                    token = token_found
                    position = new_position
            else:
                index_transition += 1

        return (False, None, position) if token is None else (True, token, position)

    def add_transition(self, transition: AutomatonTransition):
        self.__transitions.append(transition)
