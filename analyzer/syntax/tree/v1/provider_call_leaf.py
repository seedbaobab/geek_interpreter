from typing import Optional

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.tree.v1.identifier_leaf import IdentifierLeaf
from analyzer.syntax.tree.v1.service_call_branch import ServiceCallBranch


class ProviderCallLeaf(AbstractTree):

    def __init__(self):
        super().__init__(TypologyV1.PROVIDER_CALL)
        self.__identifier: Optional[IdentifierLeaf] = None
        self.__service: Optional[ServiceCallBranch] = None

    @property
    def identifier(self) -> Optional[IdentifierLeaf]:
        return self.__identifier

    @identifier.setter
    def identifier(self, value: IdentifierLeaf):
        self.__identifier = value

    @property
    def service(self) -> Optional[ServiceCallBranch]:
        return self.__service

    @service.setter
    def service(self, value: ServiceCallBranch):
        self.__service = value

    def to_str(self):
        result: str = "-- {0}\n".format(super().to_str())
        result += "{0}\n".format(self.__identifier.to_str())
        result += "{0}".format(self.__service.to_str())

        return result
