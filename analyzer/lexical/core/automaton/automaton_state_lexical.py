from typing import Optional

from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical
from analyzer.lexical.core.automaton.i_automaton_state_lexical import IAutomatonStateLexical


class AutomatonStateLexical(IAutomatonStateLexical):

    def __init__(self, is_final: bool):
        super().__init__(is_final)
        self.__transitions: list[AutomatonTransitionLexical] = []

    def extract_token(self, characters: list[str], position: int, max_position: int, token: Optional[str] = None) \
            -> tuple[bool, int, Optional[str]]:
        print("POSITION : " + str(position))
        print("MAX : " + str(max_position))
        if position.__ge__(max_position):
            if max_position.__ge__(position):
                print("MAX POSITION REACH ")
                if self._is_final:
                    print("STATE IS FINAL")
            return (True, position, token) if self._is_final else (False, position, None)

        success: bool = False
        transition_position: int = 0
        transition_max: int = len(self.__transitions)

        while transition_position.__lt__(transition_max) and position.__lt__(max_position) and not success:
            transition: AutomatonTransitionLexical = self.__transitions[transition_position]
            if transition.is_valid(characters[position]):
                print("TRANSITION VALID ON :" + characters[position])
                (success, new_position, new_token) = transition.destination.extract_token(
                    characters, (position + 1), max_position, characters[position] if token is None
                    else token + characters[position])
                if success:
                    print("NEW POSITION : " + str(new_position))
                    position = new_position
                    token = new_token
            else:
                print("TRANSITION NOT VALID ON :" + characters[position])
                transition_position += 1

        if (token is not None and self._is_final) or success:
            print("AUTOMATON VALID " + str((True, position, token)))
        else:
            print("AUTOMATON NOT VALID " + str((False, position, None)))
        return (True, position, token) if (token is not None and self._is_final) or success else (False, position, None)

    def add_transition(self, transition: AutomatonTransitionLexical):
        self.__transitions.append(transition)
