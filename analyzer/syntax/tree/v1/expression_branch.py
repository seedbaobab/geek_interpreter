from analyzer.core.typology.typology import Typology
from analyzer.syntax.core.tree.abstract_tree import AbstractTree


class ExpressionBranch(AbstractTree):
    def __init__(self, typology: Typology):
        super().__init__(typology)
