from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.tree.v1.expression_branch import ExpressionBranch


class IdentifierLeaf(ExpressionBranch):
    def __init__(self, token: TokenModel):
        super().__init__(TypologyV1.STRING)
        self.__token: TokenModel = token

    def to_str(self):
        return "{0} | {1}".format(super().to_str(), self.__token.value)
