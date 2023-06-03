from typing import Optional

from model.symbol_model import SymbolModel


class SymbolTable:

    def __init__(self):
        self.__table: dict[str, SymbolModel] = {}
        self.__scopes: dict[str, SymbolTable] = {}

    def insert(self, name: str, typology: str, return_value: Optional[str] = None):
        self.__table[name] = SymbolModel(name, typology, typology) if return_value is None \
            else SymbolModel(name, typology, return_value)

    def add_scope(self, name: str):
        self.__scopes[name] = SymbolTable()

    def lookup(self, name: str) -> Optional[SymbolModel]:
        return self.__table[name] if name in self.__table.keys() else None
    