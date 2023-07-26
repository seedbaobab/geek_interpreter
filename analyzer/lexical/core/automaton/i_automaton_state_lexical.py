from abc import ABC, abstractmethod
from typing import Optional


class IAutomatonStateLexical(ABC):
    """
    Contract class for all lexical states.
    """

    def __init__(self, is_final: bool):
        """
        Initialize a new instance of 'IAutomatonStateLexical' class.
        :param is_final: Indicate if the state is final or not.
        """
        self._is_final: bool = is_final

    @abstractmethod
    def extract_token(self, characters: list[str], position: int, max_position: int, token: Optional[str] = None) \
            -> tuple[bool, int, Optional[str]]:
        """
        Extract a token.
        :param characters: The command convert in the character list.
        :param position: The position of the analyzer.
        :param max_position: The maximum position for the analyzer.
        :param token: The token in progress.
        :return: A tuple composed of one boolean to True if a token has been found otherwise False.
        And the token found or None.
        """
        pass
