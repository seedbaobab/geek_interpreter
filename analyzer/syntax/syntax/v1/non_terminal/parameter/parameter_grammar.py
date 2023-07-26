from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.target import Target
from analyzer.syntax.core.grammar.non_terminal.alternative_grammar import AlternativeGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.syntax.v1.non_terminal.expression_grammar import ExpressionGrammar
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.syntax.v1.non_terminal.parameter.parameter_list_grammar import ParameterListGrammar
from analyzer.syntax.tree.v1.expression_branch import ExpressionBranch
from analyzer.syntax.tree.v1.parameter_branch import ParameterBranch


class ParameterGrammar(AlternativeGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.PARAMETER)

        self._sequence.append(TransitionGrammar(ExpressionGrammar(), [TypologyV1.STRING, TypologyV1.INTEGER]))
        self._sequence.append(TransitionGrammar(ParameterListGrammar(), [TypologyV1.STRING, TypologyV1.INTEGER]))

    def extract_leaf(self, target: Target) -> AbstractTree:
        if target.token.typology.__eq__(TypologyV1.CLOSE_PARENTHESIS.value):
            return ParameterBranch()

        leaf: AbstractTree = super().extract_leaf(target)

        if isinstance(leaf, ExpressionBranch):
            branch: ParameterBranch = ParameterBranch()
            branch.add_parameter(leaf)
            return branch

        return leaf
