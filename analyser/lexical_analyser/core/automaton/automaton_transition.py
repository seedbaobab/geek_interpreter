import re

from analyser.lexical_analyser.core.automaton.i_automaton_state import IAutomatonState


class AutomatonTransition:

    def __init__(self, destination: IAutomatonState, value: str):
        self.__destination: IAutomatonState = destination
        self.__value: str = value

    @property
    def destination(self):
        return self.__destination

    def is_valid(self, character: str) -> bool:
        return re.match(self.__value, character) is not None
