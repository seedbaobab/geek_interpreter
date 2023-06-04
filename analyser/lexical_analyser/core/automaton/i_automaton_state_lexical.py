from abc import ABC
from typing import Optional


class IAutomatonStateLexical(ABC):

    def __init__(self, is_final: bool):
        self._is_final: bool = is_final

    def extract_token(self, characters: list[str], position: int, max_position: int, token: Optional[str] = None) \
            -> tuple[bool, int, Optional[str]]:
        pass
