from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class IntegerLexical(AutomatonLexical, ABC):
    """
    Integer lexical unit class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'IntegerLexical' class.
        """
        super().__init__(TypologyV1.INTEGER)

    def _init(self):
        """
        Initialize the lexical unit.
        """
        self.source_state = AutomatonStateLexical(True)
        self.source_state.add_transition(AutomatonTransitionLexical(self.source_state, "\\d"))
