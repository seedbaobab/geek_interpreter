from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class StringLexical(AutomatonLexical, ABC):
    """
    String lexical unit class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'StringLexical' class.
        """
        super().__init__(TypologyV1.STRING)

    def _init(self):
        """
        Initialize the lexical unit.
        """
        self.source_state = AutomatonStateLexical(False)

        step: AutomatonStateLexical = AutomatonStateLexical(False)
        final: AutomatonStateLexical = AutomatonStateLexical(True)

        step.add_transition(AutomatonTransitionLexical(step, "[^\"]"))
        step.add_transition(AutomatonTransitionLexical(final, "\""))
        self.source_state.add_transition(AutomatonTransitionLexical(step, "\""))
