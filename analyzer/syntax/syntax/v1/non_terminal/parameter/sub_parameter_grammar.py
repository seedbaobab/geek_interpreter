from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.target import Target
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.exception.syntax_analyser_exception import SyntaxAnalyzerException
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.core.grammar.non_terminal.sequential_grammar import SequentialGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.syntax.v1.non_terminal.expression_grammar import ExpressionGrammar
from analyzer.syntax.syntax.v1.terminal.comma_grammar import CommaGrammar
from analyzer.syntax.tree.v1.parameter_branch import ParameterBranch


class SubParameterGrammar(SequentialGrammar, ABC):
    """
    Grammar class for a service class sublist of parameter.
    """

    def __init__(self):
        """
        Initialize a new instance of 'SubParameterGrammar' class.
        """
        super().__init__(TypologyV1.PARAMETER_SUBLIST)

        self._sequence.append(TransitionGrammar(CommaGrammar(), [TypologyV1.COMMA]))
        self._sequence.append(TransitionGrammar(ExpressionGrammar(), [TypologyV1.STRING, TypologyV1.INTEGER]))

    def extract_leaf(self, target: Target) -> AbstractTree:
        """
        Extract the abstract tree linked to the grammar.
        :param target: The token target.
        :return: The abstract tree linked to the grammar.
        """
        branch: AbstractTree = super().extract_leaf(target)
        if target.token.typology.__eq__(TypologyV1.CLOSE_PARENTHESIS.value):
            return branch
        branch.parameters = self.extract_leaf(target)
        return branch

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        """
        Extract the abstract tree linked to the grammar.
        :return: The abstract tree linked to the grammar.
        """
        return ParameterBranch()

    def _set_branch(self, branch: AbstractTree, position: int, leaf: AbstractTree, target: Target):
        """
        Set the elements of a branch.
        :param branch: The branch which we want to set the elements.
        :param position: The position in the sequence.
        :param leaf: The element to set in the branch.
        :param target: The target.
        """
        if not isinstance(branch, ParameterBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected {3} here."
                                          .format(message, target.command, space, self.typology.lower()))
        if position.__eq__(0):
            return
        elif position.__eq__(1):
            branch.add_parameter(leaf)
