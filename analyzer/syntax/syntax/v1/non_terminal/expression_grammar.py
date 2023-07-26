from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.core.grammar.non_terminal.alternative_grammar import AlternativeGrammar
from analyzer.syntax.syntax.v1.terminal.integer_grammar import IntegerGrammar
from analyzer.syntax.syntax.v1.terminal.string_grammar import StringGrammar


class ExpressionGrammar(AlternativeGrammar, ABC):

    def __init__(self):
        super().__init__(TypologyV1.EXPRESSION)

        # self._sequence.append(TransitionGrammar(TypologyV1.IDENTIFIER, IdentifierGrammar()))
        self._sequence.append(TransitionGrammar(IntegerGrammar(), [TypologyV1.INTEGER]))
        self._sequence.append(TransitionGrammar(StringGrammar(), [TypologyV1.STRING]))
