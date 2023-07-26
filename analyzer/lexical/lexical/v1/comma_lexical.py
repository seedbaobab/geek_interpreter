from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class CommaLexical(AutomatonLexical, ABC):
    """
    Comma lexical unit class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'CommaLexical' class.
        """
        super().__init__(TypologyV1.COMMA)

    def _init(self):
        """
        Initialize the lexical unit.
        """
        self.source_state = AutomatonStateLexical(False)
        self.source_state.add_transition(AutomatonTransitionLexical(AutomatonStateLexical(True), ","))
