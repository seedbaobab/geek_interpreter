from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.target import Target
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.exception.syntax_analyser_exception import SyntaxAnalyzerException
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.core.grammar.non_terminal.sequential_grammar import SequentialGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.syntax.v1.non_terminal.service_call.service_call_parameter_grammar import \
    ServiceCallParameterGrammar
from analyzer.syntax.syntax.v1.terminal.identifier_grammar import IdentifierGrammar
from analyzer.syntax.syntax.v1.terminal.open_parenthesis_grammar import OpenParenthesisGrammar
from analyzer.syntax.tree.v1.close_parenthensis_leaf import CloseParenthesisLeaf
from analyzer.syntax.tree.v1.identifier_leaf import IdentifierLeaf
from analyzer.syntax.tree.v1.open_parenthensis_leaf import OpenParenthesisLeaf
from analyzer.syntax.tree.v1.parameter_branch import ParameterBranch
from analyzer.syntax.tree.v1.service_call_branch import ServiceCallBranch


class ServiceCall(SequentialGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.SERVICE_CALL)

        self._sequence.append(TransitionGrammar(IdentifierGrammar(), [TypologyV1.IDENTIFIER]))
        self._sequence.append(TransitionGrammar(OpenParenthesisGrammar(), [TypologyV1.OPEN_PARENTHESIS]))
        self._sequence.append(TransitionGrammar(ServiceCallParameterGrammar(),
                                                [TypologyV1.STRING, TypologyV1.INTEGER, TypologyV1.CLOSE_PARENTHESIS]))

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        return ServiceCallBranch()

    def _set_branch(self, branch: AbstractTree, position: int, leaf: AbstractTree, target: Target):
        if not isinstance(branch, ServiceCallBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected {3} here."
                                          .format(message, target.command, space, self.typology.lower()))

        elif position.__eq__(0):
            self.__set_branch_identifier(branch, leaf, target)

        elif position.__eq__(1):
            self.__set_branch_open_parenthesis(leaf, target)

        elif position.__eq__(2):
            self.__set_branch_parameters(branch, leaf, target)

    def __set_branch_identifier(self, branch: ServiceCallBranch, leaf: AbstractTree, target: Target):
        if not isinstance(leaf, IdentifierLeaf):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected the service name here."
                                          .format(message, target.command, space))

        branch.identifier = leaf

    def __set_branch_open_parenthesis(self, leaf, target):
        if not isinstance(leaf, OpenParenthesisLeaf):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected '(' here."
                                          .format(message, target.command, space, self.typology.lower()))

    def __set_branch_parameters(self, branch: ServiceCallBranch, leaf: AbstractTree, target: Target):
        if isinstance(leaf, CloseParenthesisLeaf):
            return

        elif isinstance(leaf, ParameterBranch):
            branch.parameters = leaf

        else:
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected an 'expression' or ')' here."
                                          .format(message, target.command, space))
