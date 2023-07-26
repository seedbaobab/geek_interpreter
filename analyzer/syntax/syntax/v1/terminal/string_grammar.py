from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.grammar.terminal.terminal_grammar import TerminalGrammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.tree.v1.string_leaf import StringLeaf


class StringGrammar(TerminalGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.STRING)

    def _get_leaf(self, token: TokenModel) -> AbstractTree:
        return StringLeaf(token)