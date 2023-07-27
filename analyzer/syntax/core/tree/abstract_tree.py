from abc import ABC

from analyzer.core.typology.typology import Typology


class AbstractTree(ABC):
    """
    The abstract tree base.
    """
    
    def __init__(self, typology: Typology):
        """
        Initialize a new instance of 'AbstractTree' class.
        :param typology: The abstract tree type.
        """
        self.__typology: Typology = typology

    @property
    def typology(self) -> Typology:
        """
        Get the abstract tree type.
        :return: The abstract tree type.
        """
        return self.__typology

    def to_str(self):
        """
        Get the String format of the abstract tree.
        :return: The String format of the abstract tree.
        """
        return "{0}".format(self.__typology.value)
