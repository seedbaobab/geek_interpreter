import re

from analyzer.lexical.core.automaton.i_automaton_state_lexical import IAutomatonStateLexical


class AutomatonTransitionLexical:

    def __init__(self, destination: IAutomatonStateLexical, value: str):
        self.__destination: IAutomatonStateLexical = destination
        self.__value: str = value

    @property
    def destination(self) -> IAutomatonStateLexical:
        return self.__destination

    def is_valid(self, character: str) -> bool:
        return re.match(self.__value, character) is not None
