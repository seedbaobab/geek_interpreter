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

    def __init__(self):
        super().__init__(TypologyV1.PARAMETER_SUBLIST)

        self._sequence.append(TransitionGrammar(CommaGrammar(), [TypologyV1.COMMA]))
        self._sequence.append(TransitionGrammar(ExpressionGrammar(), [TypologyV1.STRING, TypologyV1.INTEGER]))

    def extract_leaf(self, target: Target) -> AbstractTree:
        branch: AbstractTree = super().extract_leaf(target)
        if target.token.typology.__eq__(TypologyV1.CLOSE_PARENTHESIS.value):
            return branch
        branch.parameters = self.extract_leaf(target)
        return branch

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        return ParameterBranch()

    def _set_branch(self, branch: AbstractTree, position: int, leaf: AbstractTree, target: Target):
        if not isinstance(branch, ParameterBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected {3} here."
                                          .format(message, target.command, space, self.typology.lower()))
        if position.__eq__(0):
            return
        elif position.__eq__(1):
            branch.add_parameter(leaf)
