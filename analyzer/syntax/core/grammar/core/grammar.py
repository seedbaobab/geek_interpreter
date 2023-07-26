from abc import abstractmethod, ABC

from analyzer.core.typology.typology import Typology
from analyzer.lexical.token.target import Target
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.tree.abstract_tree import AbstractTree


class Grammar(ABC):
    """
    Core class for a grammar.
    """

    def __init__(self, typology: Typology):
        """
        Initialize a new instance of 'Grammar' class.
        :param typology: The type of the grammar.
        """
        self.__typology: Typology = typology

    @property
    def typology(self) -> str:
        """
        Get the type of the grammar.
        :return: The type of the grammar.
        """
        return self.__typology.value

    @abstractmethod
    def extract_leaf(self, target: Target) -> AbstractTree:
        """
        Extract the abstract tree linked to the grammar.
        :param target: The token target.
        :return: The abstract tree linked to the grammar.
        """
        pass

    @abstractmethod
    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        """
        Generate the grammar abstract tree.
        :param token: The token used for the abstract tree.
        :return: The abstract tree generates.
        """
        pass
