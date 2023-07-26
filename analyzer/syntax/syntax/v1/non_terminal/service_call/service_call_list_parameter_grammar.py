from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.target import Target
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.exception.syntax_analyser_exception import SyntaxAnalyzerException
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.core.grammar.non_terminal.sequential_grammar import SequentialGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.syntax.v1.non_terminal.parameter.parameter_grammar import ParameterGrammar
from analyzer.syntax.syntax.v1.terminal.close_parenthesis_grammar import CloseParenthesisGrammar
from analyzer.syntax.tree.v1.close_parenthensis_leaf import CloseParenthesisLeaf
from analyzer.syntax.tree.v1.parameter_branch import ParameterBranch


class ServiceCallListParameterGrammar(SequentialGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.SERVICE_CALL_LIST)

        self._sequence.append(TransitionGrammar(ParameterGrammar(), [TypologyV1.STRING, TypologyV1.INTEGER]))
        self._sequence.append(TransitionGrammar(CloseParenthesisGrammar(), [TypologyV1.CLOSE_PARENTHESIS]))

    def _set_branch(self, branch: AbstractTree, position: int, leaf: AbstractTree, target: Target):
        if position.__eq__(0):
            self.__set_parameter(branch, leaf, target)
        elif position.__eq__(1):
            self.__set_close_parenthesis(leaf, target)

    def __set_parameter(self, branch: AbstractTree, leaf: AbstractTree, target: Target):
        if not isinstance(leaf, ParameterBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected an expression for argument here."
                                          .format(message, target.command, space))

        branch.parameters = leaf.parameters

    def __set_close_parenthesis(self, leaf: AbstractTree, target: Target):
        if not isinstance(leaf, CloseParenthesisLeaf):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected an close parenthesis here."
                                          .format(message, target.command, space))

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        return ParameterBranch()
