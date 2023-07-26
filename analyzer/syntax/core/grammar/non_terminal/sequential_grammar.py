from abc import ABC, abstractmethod

from analyzer.core.typology.typology import Typology
from analyzer.lexical.token.target import Target
from analyzer.syntax.core.exception.syntax_analyser_exception import SyntaxAnalyzerException
from analyzer.syntax.core.grammar.non_terminal.non_terminal_grammar import NonTerminalGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree


class SequentialGrammar(NonTerminalGrammar, ABC):
    """
    An grammar sequential.
    """

    def __init__(self, typology: Typology):
        """
        Initialize a new instance of 'SequentialGrammar' class.
        :param typology: The grammar type.
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

        branch: AbstractTree = self._get_leaf(target.token)

        index: int = 0
        maximum: int = len(self._sequence)

        try:
            while index.__lt__(maximum) and self._sequence[index].can_transit(target.token):
                self._set_branch(branch, index, self._sequence[index].destination.extract_leaf(target), target)
                index += 1
        except SyntaxAnalyzerException as e:
            target.index = cursor
            raise e

        if index.__lt__(maximum):
            message: str = "Your command is incorrect here: "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            target.index = cursor
            raise SyntaxAnalyzerException("{0}{1}\n{2}"
                                          .format(message, target.command, space))

        return branch

    @abstractmethod
    def _set_branch(self, branch: AbstractTree, position: int, leaf: AbstractTree, target: Target):
        """
        Set the elements of a branch.
        :param branch: The branch which we want to set the elements.
        :param position: The position in the sequence.
        :param leaf: The element to set in the branch.
        :param target: The target.
        """
        pass
