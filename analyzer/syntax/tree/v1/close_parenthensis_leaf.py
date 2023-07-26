from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.tree.abstract_tree import AbstractTree


class CloseParenthesisLeaf(AbstractTree):
    def __init__(self, token: TokenModel):
        super().__init__(TypologyV1.CLOSE_PARENTHESIS)
        self.__token: TokenModel = token


