from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.tree.v1.expression_branch import ExpressionBranch


class ParameterBranch(AbstractTree):

    def __init__(self):
        super().__init__(TypologyV1.PARAMETER)
        self.__parameters: list[ExpressionBranch] = []

    @property
    def parameters(self) -> list[ExpressionBranch]:
        return self.__parameters

    @parameters.setter
    def parameters(self, value: list[ExpressionBranch]):
        self.__parameters = self.__parameters + value

    def add_parameter(self, leaf: AbstractTree):
        self.__parameters.append(leaf)

    def to_str(self):
        result: str = "-- {0}\n".format(super().to_str())
        for expression in self.__parameters:
            result += "{0} |".format(expression.to_str())
        return result
