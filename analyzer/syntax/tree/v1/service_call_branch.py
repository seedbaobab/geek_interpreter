from typing import Optional

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.tree.v1.identifier_leaf import IdentifierLeaf
from analyzer.syntax.tree.v1.parameter_branch import ParameterBranch


class ServiceCallBranch(AbstractTree):

    def __init__(self):
        super().__init__(TypologyV1.SERVICE_CALL)
        self.__identifier: Optional[IdentifierLeaf] = None
        self.__parameters: Optional[ParameterBranch] = None

    @property
    def identifier(self) -> Optional[IdentifierLeaf]:
        return self.__identifier

    @identifier.setter
    def identifier(self, value: IdentifierLeaf):
        self.__identifier = value

    @property
    def parameters(self) -> Optional[ParameterBranch]:
        return self.__parameters

    @parameters.setter
    def parameters(self, value: ParameterBranch):
        self.__parameters = value

    def to_str(self):
        result: str = "-- {0}\n".format(super().to_str())
        result += "{0}\n".format(self.__identifier.to_str())
        if self.parameters is not None:
            result += "{0}\n".format(self.__parameters.to_str())
        return result
