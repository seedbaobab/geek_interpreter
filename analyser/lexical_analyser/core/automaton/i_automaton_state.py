from abc import abstractmethod, ABC


class IAutomatonState(ABC):

    def __init__(self, is_final: bool):
        self.__is_final: bool = is_final

    @property
    def is_final(self):
        return self.__is_final

    @abstractmethod
    def get_token(self, characters: list[str], position: int, maximum_characters: int, token: str = None):
        pass
