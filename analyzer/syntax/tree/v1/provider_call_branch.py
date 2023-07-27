from typing import Optional

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.tree.v1.identifier_leaf import IdentifierLeaf
from analyzer.syntax.tree.v1.service_call_branch import ServiceCallBranch


class ProviderCallBranch(AbstractTree):
    """
    The provider calls an abstract tree.
    """

    def __init__(self):
        """
        Initialize a new instance of 'ProviderCallBranch' class.
        """
        super().__init__(TypologyV1.PROVIDER_CALL)
        self.__identifier: Optional[IdentifierLeaf] = None
        self.__service: Optional[ServiceCallBranch] = None

    @property
    def identifier(self) -> Optional[IdentifierLeaf]:
        """
        Get the provider identifier abstract tree.
        :return: The provider identifier abstract tree.
        """
        return self.__identifier

    @identifier.setter
    def identifier(self, value: IdentifierLeaf):
        """
        Set the provider identifier abstract tree.
        :param value: The provider identifier value.
        """
        self.__identifier = value

    @property
    def service(self) -> Optional[ServiceCallBranch]:
        """
        Get the provider's service abstract tree.
        :return: The provider's service abstract tree.
        """
        return self.__service

    @service.setter
    def service(self, value: ServiceCallBranch):
        """
        Set the provider's service abstract tree.
        :param value: The new value of the provider's service abstract tree.
        """
        self.__service = value

    def to_str(self):
        """
        Get the String format of the abstract tree.
        :return: The String format of the abstract tree.
        """
        result: str = "-- {0}\n".format(super().to_str())
        result += "{0}\n".format(self.__identifier.to_str())
        result += "{0}".format(self.__service.to_str())

        return result
