from analyzer.core.typology.typology import Typology


class TypologyV1(Typology):
    """
    Enumeration for available typology for interpreter version 1.0.0.
    """

    AXIOM = "AXIOM"

    FINAL = "FINAL"

    POINT: str = "POINT"

    SPACE: str = "SPACE"

    COMMA: str = "COMMA"

    STRING: str = "STRING"

    INTEGER: str = "INTEGER"

    UNDERSCORE: str = "UNDERSCORE"

    IDENTIFIER: str = "IDENTIFIER"

    OPEN_PARENTHESIS: str = "OPEN_PARENTHESIS"

    CLOSE_PARENTHESIS: str = "CLOSE_PARENTHESIS"

    EXPRESSION: str = "EXPRESSION"

    PARAMETER: str = "PARAMETER"

    PARAMETER_LIST: str = "PARAMETER_LIST"

    PARAMETER_SUBLIST: str = "PARAMETER_SUBLIST"

    API_CALL: str = "API_CALL"

    PROVIDER_CALL: str = "PROVIDER_CALL"

    SERVICE_CALL: str = "SERVICE_CALL"

    SERVICE_CALL_LIST: str = "SERVICE_CALL_LIST"

    SERVICE_CALL_PARAMETER: str = "SERVICE_CALL_PARAMETER"
