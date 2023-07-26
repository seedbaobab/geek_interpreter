from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.target import Target
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.exception.syntax_analyser_exception import SyntaxAnalyzerException
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.core.grammar.non_terminal.sequential_grammar import SequentialGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.syntax.v1.non_terminal.expression_grammar import ExpressionGrammar
from analyzer.syntax.syntax.v1.non_terminal.parameter.sub_parameter_grammar import SubParameterGrammar
from analyzer.syntax.tree.v1.expression_branch import ExpressionBranch
from analyzer.syntax.tree.v1.parameter_branch import ParameterBranch


class ParameterListGrammar(SequentialGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.PARAMETER_LIST)

        self._sequence.append(TransitionGrammar(ExpressionGrammar(), [TypologyV1.STRING, TypologyV1.INTEGER]))
        self._sequence.append(TransitionGrammar(SubParameterGrammar(), [TypologyV1.COMMA]))

    def _set_branch(self, branch: AbstractTree, position: int, leaf: AbstractTree, target: Target):
        if not isinstance(branch, ParameterBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected {3} here."
                                          .format(message, target.command, space, self.typology.lower()))

        if position.__eq__(0):
            self.__set_expression(branch, leaf, target)

        elif position.__eq__(1):
            self.__set_parameter(branch, leaf, target)

    def __set_expression(self, branch: ParameterBranch, leaf: AbstractTree, target: Target):
        if not isinstance(leaf, ExpressionBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nExpected list of arguments or ')' here."
                                          .format(message, target.command, space, self.typology.lower()))

        branch.add_parameter(leaf)

    def __set_parameter(self, branch: ParameterBranch, leaf: AbstractTree, target: Target):
        if not isinstance(leaf, ParameterBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nExpected list of arguments or ')' here."
                                          .format(message, target.command, space, self.typology.lower()))
        branch.parameters = leaf.parameters

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        return ParameterBranch()
