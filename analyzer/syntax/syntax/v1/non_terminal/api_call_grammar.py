from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.target import Target
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.exception.syntax_analyser_exception import SyntaxAnalyzerException
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.core.grammar.non_terminal.sequential_grammar import SequentialGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.syntax.v1.non_terminal.provider_call_grammar import ProviderCallGrammar
from analyzer.syntax.syntax.v1.terminal.identifier_grammar import IdentifierGrammar
from analyzer.syntax.syntax.v1.terminal.point_grammar import PointGrammar
from analyzer.syntax.tree.v1.identifier_leaf import IdentifierLeaf
from analyzer.syntax.tree.v1.point_leaf import PointLeaf
from analyzer.syntax.tree.v1.provider_call_branch import ProviderCallBranch
from analyzer.syntax.tree.v1.service_call_branch import ServiceCallBranch


class ApiCallGrammar(SequentialGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.PROVIDER_CALL)

        self._sequence.append(TransitionGrammar(IdentifierGrammar(), [TypologyV1.IDENTIFIER]))
        self._sequence.append(TransitionGrammar(PointGrammar(), [TypologyV1.POINT]))
        self._sequence.append(TransitionGrammar(ProviderCallGrammar(), [TypologyV1.IDENTIFIER]))

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        return ProviderCallBranch()

    def _set_branch(self, branch: AbstractTree, position: int, leaf: AbstractTree, target: Target):
        if not isinstance(branch, ProviderCallBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected a provider name here."
                                          .format(message, target.command, space))

        elif position.__eq__(0):
            self.__set_identifier(branch, leaf, target)

        elif position.__eq__(1):
            self.__set_point(leaf, target)

        elif position.__eq__(2):
            self.__set_service_call(branch, leaf, target)

    def __set_identifier(self, branch: ProviderCallBranch, leaf: AbstractTree, target: Target):
        if not isinstance(leaf, IdentifierLeaf):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected a provider name here."
                                          .format(message, target.command, space))

        branch.identifier = leaf

    def __set_point(self, leaf, target):
        if not isinstance(leaf, PointLeaf):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected a '.' here."
                                          .format(message, target.command, space))

    def __set_service_call(self, branch: ProviderCallBranch, leaf: AbstractTree, target: Target):
        if not isinstance(leaf, ServiceCallBranch):
            message: str = "Your command is incorrect : "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command expected a provider name here."
                                          .format(message, target.command, space))

        branch.service = leaf
