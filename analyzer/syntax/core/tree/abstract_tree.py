from abc import abstractmethod, ABC

from analyzer.core.typology.typology import Typology


class AbstractTree(ABC):
    
    def __init__(self, typology: Typology):
        self.__typology: Typology = typology

    @property
    def typology(self) -> Typology:
        return self.__typology

    def to_str(self):
        return "{0}".format(self.__typology.value)
