class TokenModel:
    def __init__(self, typology: str, value: str, start: int, end: int):
        self.__typology: str = typology
        self.__value: str = value
        self.__end: int = end
        self.__start: int = start
        self.__size: int = len(value)

    @property
    def typology(self) -> str:
        return self.__typology

    @property
    def value(self) -> str:
        return self.__value

    @property
    def start(self) -> int:
        return self.__start

    @property
    def end(self) -> int:
        return self.__end

    @property
    def size(self) -> int:
        return self.__size

    def to_str(self) -> str:
        return "== TOKEN '{0}' | value: '{1}'".format(self.__typology, self.__value)
