from abc import ABC

from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class SpaceLexical(AutomatonLexical, ABC):
    """
    Space lexical unit class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'SpaceLexical' class.
        """
        super().__init__("SPACE")

    def _init(self):
        """
        Initialize the lexical unit.
        """
        self.source_state = AutomatonStateLexical(False)
        self.source_state.add_transition(AutomatonTransitionLexical(AutomatonStateLexical(True), "\\s"))
