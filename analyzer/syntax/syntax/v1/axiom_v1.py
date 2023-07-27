from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar
from analyzer.syntax.core.grammar.non_terminal.alternative_grammar import AlternativeGrammar
from analyzer.syntax.syntax.v1.non_terminal.provider_call_grammar import ProviderCallGrammar


class AxiomV1(AlternativeGrammar):
    """
    Version one of the geek language axioms.
    """

    def __init__(self):
        """
        Initialize a new instance of 'AxiomV1' class.
        """
        super().__init__(TypologyV1.AXIOM)
        self._sequence.append(TransitionGrammar(ProviderCallGrammar(), [TypologyV1.IDENTIFIER]))
