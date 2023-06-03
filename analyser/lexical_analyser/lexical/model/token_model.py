class TokenModel:

    def __init__(self, typology: str, token: str, start: int, end: int):
        self.__typology: str = typology
        self.__token: str = token
        self.__start: int = start
        self.__end: int = end
        self.__length: int = len(token)

    @property
    def typology(self) -> str:
        return self.__typology

    @property
    def token(self):
        return self.__token

    @property
    def start(self) -> int:
        return self.__start

    def to_str(self):
        return "== TOKEN '{1}' | TYPE: '{0}' | START POSITION: {2} | END POSITION: {3} | SIZE: {4}"\
            .format(self.__typology, self.__token, str(self.__start), str(self.__end), str(self.__length))
