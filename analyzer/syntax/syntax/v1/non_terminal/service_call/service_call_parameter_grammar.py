from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.core.grammar.non_terminal.alternative_grammar import AlternativeGrammar
from analyzer.syntax.syntax.v1.non_terminal.service_call.service_call_list_parameter_grammar import \
    ServiceCallListParameterGrammar
from analyzer.syntax.syntax.v1.terminal.close_parenthesis_grammar import CloseParenthesisGrammar


class ServiceCallParameterGrammar(AlternativeGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.SERVICE_CALL_PARAMETER)

        self._sequence.append(TransitionGrammar(ServiceCallListParameterGrammar(),
                                                [TypologyV1.STRING, TypologyV1.INTEGER]))
        self._sequence.append(TransitionGrammar(CloseParenthesisGrammar(), [TypologyV1.CLOSE_PARENTHESIS]))
