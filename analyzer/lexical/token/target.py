from analyzer.lexical.token.token import TokenModel


class Target:
    """
    Target to
    """

    def __init__(self, command: str, tokens: list[TokenModel]):
        """
        Initialize a new instance of 'Target' class.
        :param command: The complete command
        :param tokens: The command in token list.
        """
        self.__tokens: list[TokenModel] = tokens
        self.__maximum: int = len(self.__tokens)
        self.__command: str = command
        self.__index: int = 0

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, value: int):
        self.__index = value

    @property
    def position(self) -> int:
        """
        Get the target cursor current position.
        :return: The target cursor current position.
        """
        return self.__index

    @property
    def is_finish(self) -> bool:
        """
        Indicate if the target is finished to analyze.
        :return: True if the target is finished to parse.
        """
        return self.__index.__ge__(self.__maximum)

    @property
    def token(self) -> TokenModel:
        """
        Get the token at the target cursor position.
        :return: The token at the target cursor position.
        """
        return self.__tokens[self.__index] if self.__index.__lt__(self.__maximum) else self.__tokens[self.__index - 1]

    @property
    def command(self) -> str:
        """
        The complete command.
        :return: The complete command.
        """
        return self.__command

    def next(self):
        """
        Push the target cursor to the next token.
        """
        self.__index += 1 if self.__index.__ne__(self.__maximum) else 0

    def previous(self):
        """
        Set the target cursor to the previous token.
        """
        self.__index -= 0 if self.__index.__eq__(0) else 1
