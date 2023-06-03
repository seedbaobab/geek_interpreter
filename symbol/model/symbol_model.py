class SymbolModel:

    def __init__(self, name: str, typology: str, return_value: str):
        self.__name: str = name
        self.__typology: str = typology
        self.__return_value: str = return_value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def typology(self) -> str:
        return self.__typology

    @property
    def return_value(self) -> str:
        return self.__return_value
