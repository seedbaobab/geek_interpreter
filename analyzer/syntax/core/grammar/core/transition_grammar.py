from analyzer.core.typology.typology import Typology
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.grammar.core.grammar import Grammar


class TransitionGrammar:
    """
    The transition between grammar.
    """

    def __init__(self, destination: Grammar, values: list[Typology]):
        """
        Initialize a new instance of 'TransitionGrammar' class.
        :param destination: The transition destination.
        :param values: The transition value.
        """
        self.__destination: Grammar = destination
        self.__values: list[Typology] = values

    @property
    def destination(self) -> Grammar:
        """
        Get the transition destination.
        :return: The transition destination.
        """
        return self.__destination

    @property
    def values(self) -> str:
        """
        Get the transition values in string format.
        :return: The transition values in string format.
        """
        result: str = ""

        index: int = 0
        maximum: int = len(self.__values)

        while index.__lt__(maximum):
            result += self.__values[index].value.lower().replace("_", " ") if index.__eq__(maximum - 1) \
                else "{0} or ".format(self.__values[index].value.lower().replace("_", " "))
            index += 1

        return result

    def can_transit(self, token: TokenModel) -> bool:
        """
        Indicate if a token can got to the transition's destination.
        :param token: The token to test.
        :return: True if the token can go to the transition destination otherwise false.
        """
        index: int = 0
        maximum: int = len(self.__values)

        while index.__lt__(maximum) and token.typology.__ne__(self.__values[index].value):
            index += 1

        return index.__lt__(maximum)
