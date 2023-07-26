from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.grammar.terminal.terminal_grammar import TerminalGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.tree.v1.point_leaf import PointLeaf


class PointGrammar(TerminalGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.POINT)

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        return PointLeaf(token)
