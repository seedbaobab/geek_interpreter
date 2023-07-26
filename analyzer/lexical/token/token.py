from analyzer.core.typology.typology import Typology


class TokenModel:
    """
    The token model class.
    """

    def __init__(self, typology: Typology, value: str, start: int, end: int):
        """
        Initialize a new instance of 'TokenModel' class.
        :param typology: The token typology.
        :param value: The token value.
        :param start: The start position of the token in the command.
        :param end: The end position of the token in the command.
        """
        self.__typology: Typology = typology
        self.__value: str = value
        self.__end: int = end
        self.__start: int = start
        self.__size: int = len(value)

    @property
    def type(self) -> Typology:
        """
        Get the token type.
        :return: The token type.
        """
        return self.__typology

    @property
    def typology(self) -> str:
        """
        Get the token typology.
        :return: The token typology.
        """
        return self.__typology.value

    @property
    def value(self) -> str:
        """
        Get the token value.
        :return: The token value.
        """
        return self.__value

    @property
    def start(self) -> int:
        """
        Get the start position of the token in the command.
        :return: The start position of the token in the command.
        """
        return self.__start

    @property
    def end(self) -> int:
        """
        Get the end position of the token in the command.
        :return: The end position of the token in the command.
        """
        return self.__end

    @property
    def size(self) -> int:
        """
        Get the size of the token value.
        :return: The size of the token value.
        """
        return self.__size

    def to_str(self) -> str:
        """
        Get the string representation of the token model class.
        :return: The string representation of the token model class.
        """
        return "TOKEN : TYPE: '{0}' | VALUE: '{1}' | SIZE: {2} | START {3} | END {4}"\
            .format(self.__typology.value, self.__value, self.__size, self.__start, self.__end)
