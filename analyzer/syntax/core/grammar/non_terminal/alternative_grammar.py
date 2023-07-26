from abc import ABC
from typing import Optional

from analyzer.core.typology.typology import Typology
from analyzer.lexical.token.target import Target
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.exception.syntax_analyser_exception import SyntaxAnalyzerException
from analyzer.syntax.core.grammar.non_terminal.non_terminal_grammar import NonTerminalGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree


class AlternativeGrammar(NonTerminalGrammar, ABC):
    """
    An grammar alternative.
    """

    def __init__(self, typology: Typology):
        """
        Initialize a new instance of 'AlternativeGrammar' class.
        :param typology: The grammar typology.
        """
        super().__init__(typology)

    def extract_leaf(self, target: Target) -> AbstractTree:
        """
        Extract the abstract tree linked to the grammar.
        :param target: The token target.
        :return: The abstract tree linked to the grammar.
        """
        self._check_precondition_extraction(target)
        cursor: int = target.index

        index: int = 0
        maximum: int = len(self._sequence)
        leaf: Optional[AbstractTree] = None

        exception: Optional[SyntaxAnalyzerException] = None

        while index.__lt__(maximum) and leaf is None:
            try:
                if self._sequence[index].can_transit(target.token):
                    leaf = self._sequence[index].destination.extract_leaf(target)
            except SyntaxAnalyzerException as e:
                exception = e
                target.index = cursor
                leaf = None

            index += 1 if leaf is None else 0

        if leaf is None:
            if exception is None:
                message: str = "Your command is incorrect : "
                space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
                raise SyntaxAnalyzerException("{0}{1}\n{2}"
                                              .format(message, target.command, space))
            raise exception

        return leaf

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        """
        Generate the grammar abstract tree.
        :param token: The token used for the abstract tree.
        :return: The abstract tree generates.
        """
        return None
