import re

from analyzer.lexical.core.automaton.i_automaton_state_lexical import IAutomatonStateLexical


class AutomatonTransitionLexical:
    """
    The automaton state transition class.
    """

    def __init__(self, destination: IAutomatonStateLexical, value: str):
        """
        Initialize a new instance of 'AutomatonTransitionLexical' class.
        :param destination: The transition destination.
        :param value: The transition value.
        """
        self.__destination: IAutomatonStateLexical = destination
        self.__value: str = value

    @property
    def destination(self) -> IAutomatonStateLexical:
        """
        Get the destination of the transition.
        :return: The destination of the transition.
        """
        return self.__destination

    def is_valid(self, character: str) -> bool:
        """
        Check if the character pass in parameter can pass the transition.
        :param character: The character to be evaluated.
        :return: True if the character can pass; otherwise False.
        """
        return re.match(self.__value, character) is not None
