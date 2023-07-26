from abc import ABC

from analyzer.core.typology.typology import Typology
from analyzer.lexical.token.target import Target
from analyzer.syntax.core.grammar.core.grammar import Grammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree


class TerminalGrammar(Grammar, ABC):
    """
    An grammar terminal.
    """

    def __init__(self, typology: Typology):
        """
        Initialize a new instance of 'TerminalGrammar' class.
        :param typology: The grammar typology.
        """
        super().__init__(typology)

    def extract_leaf(self, target: Target) -> AbstractTree:
        """
        Extract the abstract tree linked to the grammar.
        :param target: The token target.
        :return: The abstract tree linked to the grammar.
        """
        leaf: AbstractTree = self._get_leaf(target.token)
        target.next()
        return leaf
